import json
import os
from tqdm import tqdm
from src.inference.model import Model
from src.inference.prompt_loader import PromptLoader
from src.utils import DataUtil, PathUtil
from src.globals import Globals

_ONLY_PROMPT = False

class Inference:
    def __init__(self, args):
        self.start_id = args.start_id
        self.end_id = args.end_id
        self.data = DataUtil.load_data()
        self.model = Model(args.model_str, args.temperature)
        self.task_mode = args.task_mode
        self.dep_mode = args.dep_mode
        self.repeat = args.repeat
        self.name_string = PathUtil.get_name_string(args.model_str, args.task_mode, args.dep_mode, args.temperature)

    def pipeline(self):
        results = []
        for repo_data in tqdm(self.data):
            repo_id = int(repo_data['id'])
            if repo_id < self.start_id:
                continue
            if repo_id > self.end_id:
                break
            print(f"Looking into Repo-{repo_id}...")
            repo_path = os.path.join(Globals.DATASET_PATH, str(repo_id))
            repo_name = repo_data['repo_name'].split('/')[1]
            for src_file in repo_data['src_files']:
                file_path = os.path.join(repo_path, repo_name, src_file['relative_path'])
                for method in src_file['linked_methods']:
                    method_name = method['method_name']
                    tmp_prompts = []
                    tmp_reasoning_paths = []
                    tmp_raw_output = []
                    tmp_predicted = []

                    prompt_loader = PromptLoader(method, repo_path, repo_name, file_path)
                    prompts = prompt_loader.generate_prompts(self.task_mode, self.dep_mode)

                    for r in range(self.repeat):
                        if _ONLY_PROMPT:
                            tmp_prompts.append('\n'.join(prompts))
                            break

                        result = self.model.run_prompts(prompts)
                        if isinstance(result, tuple):
                            message_history = result[0]
                            tmp_reasoning_paths.append('\n'.join(result[1]))
                        else:
                            message_history = result

                        if r == 0:
                            for m in message_history:
                                try:
                                    print(m['role'] + ":\n" + m['content'] + "\n")
                                except Exception as e:
                                    print(e)
                        output = message_history[-1]["content"]

                        method_code = DataUtil.extract_function_from_output(output, method_name)
                        tmp_prompts.append('\n'.join(prompts))
                        tmp_raw_output.append(output)
                        tmp_predicted.append(method_code)

                    method['prompt'] = tmp_prompts
                    if not _ONLY_PROMPT:
                        method['raw_output'] = tmp_raw_output
                        method['predicted'] = tmp_predicted
                        method['reasoning_paths'] = tmp_reasoning_paths
                        self.save_tmp_results(method, repo_id, method_name)
            results.append(repo_data)
        self.save_results(results)
        # self.tear_down()

    def save_results(self, res):
        output_path = PathUtil.get_output_path(self.name_string)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(res, f, indent=4)

    def save_tmp_results(self, tmp_res, tmp_idx, method_name):
        tmp_output_path = PathUtil.get_tmp_output_path(self.name_string, tmp_idx, method_name)
        with open(tmp_output_path, 'w', encoding='utf-8') as f:
            json.dump(tmp_res, f, indent=4)

    def tear_down(self):
        tmp_output_path = os.path.join(Globals.RESULT_PATH, 'tmp_output')
        file_list = os.listdir(tmp_output_path)
        tmp_output_prefix = f"{self.name_string}_tmp"
        for item in file_list:
            if item.startswith(tmp_output_prefix):
                os.remove(os.path.join("tmp_output_path", item))

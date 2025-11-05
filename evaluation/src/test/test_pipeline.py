import os
import json
import shutil
import numpy as np
import pandas as pd
from src.utils import FileUtil, DataUtil, PathUtil, ProcessUtil
from src.globals import Globals


class Test:
    def __init__(self, args):
        self.start_id = args.start_id
        self.end_id = args.end_id
        self.task_mode = args.task_mode
        self.dep_mode = args.dep_mode
        self.repeat = args.repeat
        self.name_string = PathUtil.get_name_string(args.model_str, args.task_mode, args.dep_mode, args.temperature)
        output_path = PathUtil.get_output_path(self.name_string)
        self.data = FileUtil.read_json(output_path)

    def run_unittest(self, repo_id, test_path, test_module_name, test_class_name, python_path, name_string, repeat):
        script_path = './run_unittest.py'
        cmd = [python_path, script_path,
               '--repo_id', str(repo_id),
               '--test_path', test_path,
               '--test_module_name', test_module_name,
               '--test_class_name', test_class_name,
               '--name_string', name_string,
               '--repeat', str(repeat)]
        return_code, output = ProcessUtil.run_process(cmd, test_path)
        print(f"Exceptions raised during tests:\n{output.decode()}")

    def pipeline(self):
        test_results = {}
        test_names = {}
        for repo_data in self.data:
            repo_id = int(repo_data['id'])
            if repo_id < self.start_id:
                continue
            if repo_id > self.end_id:
                break
            test_results[repo_id] = {}
            test_names[repo_id] = {}
            print(f"Looking into Repo-{repo_id}...")
            repo_path = os.path.join(Globals.DATASET_PATH, str(repo_id))
            repo_name = repo_data['repo_name'].split('/')[1]
            venv_path = os.path.join(repo_path, repo_name, 'venv')
            python_path = os.path.join(venv_path, 'bin', 'python.exe')
            test_path = os.path.join(repo_path, repo_name, 'tests', 'test_adapteval')
            for src_file in repo_data['src_files']:
                file_path = os.path.join(repo_path, repo_name, src_file['relative_path'])
                file_name = src_file['file_name']
                ctx_file = os.path.join(test_path, file_name)
                if not os.path.exists(ctx_file):
                    ctx_file = os.path.join(test_path, 'ctx_' + file_name)
                    if not os.path.exists(ctx_file):
                        raise Exception("No target context file found.")
                for method in src_file['linked_methods']:
                    method_name = method['method_name']
                    # install func_timeout in the first turn
                    install_func_cmd = [str(python_path), "-m", "pip", "install", "func_timeout", "tiktoken"]
                    ProcessUtil.run_process(install_func_cmd, test_path)

                    test_module_name = '_'.join(['test', file_name.split('.')[0], method_name])
                    test_class_name = 'Test' + DataUtil.snake_to_camel(method_name)
                    res_items = []
                    content = FileUtil.read_file_as_string(ctx_file)
                    stored = content
                    for repeat in range(self.repeat):
                        output = method['predicted'][repeat]
                        replaced = DataUtil.replace_method_in_code(content, method_name, output)
                        # print(replaced)
                        try:
                            FileUtil.write_file(ctx_file, replaced)
                            self.run_unittest(repo_id, test_path, test_module_name, test_class_name, python_path,
                                              self.name_string, repeat)
                            tmp_test_path = PathUtil.get_tmp_test_file_output_path()
                            res_item_path = os.path.join(tmp_test_path, f"{repo_id}_{test_module_name}_{repeat}.json")
                            res_items.append(FileUtil.read_json(res_item_path))
                        finally:
                            FileUtil.write_file(ctx_file, stored)
                    test_results[repo_id][method_name] = res_items
                    # collect test name
                    test_code = FileUtil.read_file_as_string(os.path.join(test_path, test_module_name+'.py'))
                    lines = test_code.splitlines()
                    test_names[repo_id][method_name] = []
                    for line in lines:
                        line = line.strip()
                        if line.startswith('def test_'):
                            test_names[repo_id][method_name].append(line[4:].split('(')[0])

        print(test_results)
        # self.tear_down()
        self.save_results(test_results)

        pass_at_1, pass_at_1_adapt, overview, errors = self.evaluate_test_results(test_results, test_names, 1)
        pass_at_5, pass_at_5_adapt,  _, _ = self.evaluate_test_results(test_results, test_names, 5)
        print("pass@1:", pass_at_1)
        print("pass@5:", pass_at_5)
        print("pass@1-adapt:", pass_at_1_adapt)
        print("pass@5-adapt:", pass_at_5_adapt)
        print("overview:", overview)
        print("errors:", errors)

    def save_results(self, res):
        test_output_path = PathUtil.get_test_output_path(self.name_string)
        with open(test_output_path, 'w', encoding='utf-8') as f:
            json.dump(res, f, sort_keys=True, indent=4)

    @staticmethod
    def tear_down():
        tmp_test_path = PathUtil.get_tmp_test_file_output_path()
        file_list = os.listdir(tmp_test_path)
        for item in file_list:
            file_path = os.path.join(tmp_test_path, item)
            if "__pycache__" not in file_path:
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                else:
                    os.remove(file_path)

    @staticmethod
    def evaluate_method_test_outputs(result_dict, test_names):
        results = {}
        results['Success'] = 0
        results['Partial'] = 0
        results['Failed'] = 0
        results['TimeoutError'] = 0
        results['CompilationError'] = 0
        results['Error'] = 0
        results['Failure'] = 0
        results['Passed'] = 0
        results['Tests'] = {}
        for test_name in test_names:
            results['Tests'][test_name] = {}
        for single_result in result_dict:
            error_num = sum([len(v) for _, v in single_result['errors'].items()])
            failure_num = sum([len(v) for _, v in single_result['failures'].items()])
            if single_result['total_run'] == 0:
                if single_result['compilation'] != 'success':
                    results['CompilationError'] += 1
                    for test_name in test_names:
                        results['Tests'][test_name].setdefault('CompilationError', 0)
                        results['Tests'][test_name]['CompilationError'] += 1
                else:
                    results['TimeoutError'] += 1
                    for test_name in test_names:
                        results['Tests'][test_name].setdefault('TimeoutError', 0)
                        results['Tests'][test_name]['TimeoutError'] += 1
            else:
                results['Error'] += error_num
                results['Failure'] += failure_num
                passed = {}
                for test_name in test_names:
                    passed[test_name] = True
                if error_num + failure_num == 0:  # success
                    results['Success'] += 1
                else:  # failed tests
                    for error_type in single_result['errors']:
                        for error_test_name in single_result['errors'][error_type]:
                            results['Tests'][error_test_name].setdefault(error_type, 0)
                            results['Tests'][error_test_name][error_type] += 1
                            passed[error_test_name] = False
                    for error_type in single_result['failures']:
                        for error_test_name in single_result['failures'][error_type]:
                            results['Tests'][error_test_name].setdefault(error_type, 0)
                            results['Tests'][error_test_name][error_type] += 1
                            passed[error_test_name] = False
                    if sum(passed.values()) > 0:
                        results['Partial'] += 1
                    else:
                        results['Failed'] += 1
                results['Passed'] += sum(passed.values())
        return results

    def evaluate_test_results(self, test_results, test_names, k):
        pass_at_k_list = []
        pass_at_k = 0
        pass_at_k_adapt_list = []
        pass_at_k_adapt = 0
        overview = {'num_fail': 0, 'num_partial': 0, 'num_pass': 0, 'num_total': 0}
        errors = {'Error': 0, 'Failure': 0, 'TimeoutError': 0, 'CompilationError': 0}
        method_num = 0
        adaptation_num = 0
        for repo_id in test_results:
            for method_name in test_results[repo_id]:
                total_tmp = len(test_results[repo_id][method_name])
                method_test_names = test_names[repo_id][method_name]
                method_test_results = self.evaluate_method_test_outputs(test_results[repo_id][method_name],
                                                                        method_test_names)
                # print('=====')
                # print(method_test_results)
                pass_tmp = method_test_results['Success']
                overview['num_total'] += total_tmp
                overview['num_pass'] += method_test_results['Success']
                overview['num_partial'] += method_test_results['Partial']
                overview['num_fail'] += method_test_results['Failed']
                errors['Error'] += method_test_results['Error']
                errors['Failure'] += method_test_results['Failure']
                errors['TimeoutError'] += method_test_results['TimeoutError']
                errors['CompilationError'] += method_test_results['CompilationError']
                pass_at_k_tmp = self.pass_at_k(total_tmp, pass_tmp, k)  # if total_tmp != 0 else 0
                pass_at_k_list.append([repo_id, method_name, pass_at_k_tmp])
                pass_at_k += pass_at_k_tmp
                method_num += 1
                try:
                    for a in self.get_adaptations(repo_id, method_name):
                        associated_tests = a['associated_tests']
                        fail_tmp_a = 0
                        for t in associated_tests:
                            n_fails = sum(method_test_results['Tests'][t].values())
                            fail_tmp_a = max(fail_tmp_a, n_fails)
                        pass_at_k_tmp_a = self.pass_at_k(total_tmp, total_tmp - fail_tmp_a, k)
                        pass_at_k_adapt_list.append([repo_id, method_name, a['id'], a['title'], pass_at_k_tmp_a])
                        pass_at_k_adapt += pass_at_k_tmp_a
                        adaptation_num += 1
                except:
                    print(repo_id, method_name)
                    raise Exception
        pass_at_k = pass_at_k / method_num
        pass_at_k_adapt = pass_at_k_adapt / adaptation_num
        pass_at_k_df = pd.DataFrame(pass_at_k_list, columns=['repo_id', 'method_name', f'pass_at_{k}'])
        pass_at_k_adapt_df = pd.DataFrame(pass_at_k_adapt_list, columns=['repo_id', 'method_name', 'adaptation_id', 'adaptation_title', f'pass_at_{k}'])
        with open(PathUtil.get_test_output_path(self.name_string) + f'_pass_at_{k}.csv', 'w', encoding='utf-8') as f:
            pass_at_k_df.to_csv(f, index=False)
        with open(PathUtil.get_test_output_path(self.name_string) + f'_pass_at_{k}_adapt.csv', 'w', encoding='utf-8') as f:
            pass_at_k_adapt_df.to_csv(f, index=False)
        return pass_at_k, pass_at_k_adapt, overview, errors

    @staticmethod
    def pass_at_k(n, c, k):
        if n - c < k:
            return 1.0
        return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))

    def get_adaptations(self, repo_id, method_name):
        for repo_data in self.data:
            if repo_id == int(repo_data['id']):
                for src_file in repo_data['src_files']:
                    for method in src_file['linked_methods']:
                        if method_name == method['method_name']:
                            return method['annotated_adaptations']
        return None
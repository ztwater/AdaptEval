import os
import re
from utils import FileUtil, DataUtil


class PromptLoader:
    def __init__(self, data, repo_path, repo_name, file_path):
        self.data = data
        self.repo_path = repo_path
        self.repo_name = repo_name
        self.root_path = os.path.join(repo_path, repo_name)
        self.file_path = file_path

    def generate_reused_snippet(self):
        method_name = self.data['method_name']
        file_name = self.data['so_clone']
        if not file_name.endswith('clean.py'):
            raise Exception("The reused SO post is not executed.")
        file_path = os.path.join(self.repo_path, 'linked_posts', method_name, file_name)
        file_content = FileUtil.read_file_as_string(file_path)
        return f"### Reused Snippet:\n```python\n{file_content}\n```\n"

    def generate_infile_context(self):
        if not os.path.exists(self.file_path):
            raise Exception("No target context file found.")
        content = FileUtil.read_file_as_string(self.file_path)
        method_name = self.data['method_name']
        replaced = DataUtil.replace_method_in_code_for_infile_prompt(content, method_name, "# insert your adapted method here.\n")
        return f"### In-file Context:\n```python\n{replaced}\n```\n"

    def generate_task(self):
        task_desc_path = os.path.join(self.repo_path, f"task_desc_of_{self.data['method_name']}.txt")
        task_desc = FileUtil.read_file_as_string(task_desc_path)
        return (f"### Adaptation Task Description:\n"
                f"{task_desc}\n")
    def generate_adaptations(self):
        adaptations = self.data['annotated_adaptations']
        adaptations_with_selected_keys = []
        for a in adaptations:
            tmp = dict()
            tmp['id'] = a['id']
            tmp['type'] = a['type']
            tmp['description'] = a['description']
            adaptations_with_selected_keys.append(tmp)
        return (f"### Adaptations Required to Perform:\n"
                f"```json\n{adaptations_with_selected_keys}\n```\n")

    def generate_code_block(self, name, code):
        return f"[Start of {name}]\n```python\n{DataUtil.remove_leading_spaces(code)}\n```\n[End of {name}]"

    def generate_dependencies(self, mode='None'):
        deps = self.data['dependencies']
        code_list = []
        if mode == 'Oracle':
            class_names = [field.split('.')[0] for field in deps['in_class']['fields']]
            class_names = list(dict.fromkeys(class_names))  # remove duplicates
            for class_name in class_names:
                class_code = DataUtil.extract_class_definition(self.file_path, class_name)
                code_list.append(self.generate_code_block(class_name, class_code))
            for method in deps['in_class']['methods']:
                class_name, method_name = method.split('.')
                method_code = DataUtil.extract_method_from_class(self.file_path, class_name, method_name)
                code_list.append(self.generate_code_block(method, method_code))
            for var_name in deps['in_file']['variables']:
                var_code = DataUtil.extract_variable_from_file(self.file_path, var_name)
                code_list.append(self.generate_code_block(var_name, var_code))
            for func_name in deps['in_file']['functions']:
                func_code = DataUtil.extract_function_from_file(self.file_path, func_name)
                code_list.append(self.generate_code_block(func_name, func_code))
            for var_path in deps['in_repo']['variables']:
                rel_file_path, var_in_file = re.split('::', var_path)
                file_path = os.path.join(self.root_path, rel_file_path)
                if '.' in var_in_file:
                    class_name, var_name = var_in_file.split('.')
                    var_code = DataUtil.extract_class_definition(file_path, class_name)
                else:
                    var_code = DataUtil.extract_class_definition(file_path, var_in_file)
                    if var_code == '':
                        var_code = DataUtil.extract_variable_from_file(file_path, var_in_file)
                code_list.append(self.generate_code_block(var_path, var_code))
            for func_path in deps['in_repo']['functions']:
                rel_file_path, func_in_file = re.split('::', func_path)
                file_path = os.path.join(self.root_path, rel_file_path)
                if '.' in func_in_file:
                    class_name, func_name = func_in_file.split('.')
                    func_code = DataUtil.extract_method_from_class(file_path, class_name, func_name)
                else:
                    func_code = DataUtil.extract_function_from_file(file_path, func_in_file)
                code_list.append(self.generate_code_block(func_path, func_code))
            # import statements
            packages = [ext.split('.')[0] for ext in deps['external']]
            packages = list(dict.fromkeys(packages))
            imports = []
            for package_name in packages:
                imports += DataUtil.extract_imports_from_file(self.file_path, package_name)
            if len(imports) > 0:
                code_list.append(self.generate_code_block('Imports', '\n'.join(imports)))

            if len(code_list) == 0:
                code = "None.\n"
            else:
                code = '\n'.join(code_list)
            return f"### Related Code Context For Reference:\n{code}"
        elif mode == 'Retrieval':
            code = "None.\n"
            return f"### Related Code Context For Reference:\n{code}"
        else:
            return None


    def generate_prompts(self, task_mode=0, dep_mode='None'):
        if task_mode == 0:
            json_file = " and a json file containing required adaptations"
            description = "the description of adaptations one by one"
            reference = "Some related code context from the target code base is provided for reference."
        elif task_mode == 1:
            json_file = ""
            description = "the task description"
            reference = "Some related code context from the target code base is provided for reference."
        else:
            json_file = ""
            description = "its intra-file context"
            reference = ""
        prompt = (f"I will provide you with a code snippet to reuse{json_file}. "
                  f"You should adapt the snippet into a target code base according to {description}. "
                  f"{reference}")

        prompt += '\n\n' + self.generate_reused_snippet()
        if task_mode == 0:
            prompt += '\n\n' + self.generate_adaptations()
        elif task_mode == 1:
            prompt += '\n\n' + self.generate_task()
        else:
            prompt += '\n\n' + self.generate_infile_context()

        if task_mode < 2:
            dep_str = self.generate_dependencies(dep_mode)
            if dep_str is not None:
                prompt += '\n\n' + dep_str

        prompt += ("\n\nPlease write out function after adaptation in the following section:\n"
                   "### Adapted Function:")

        return [prompt]


import os
import re
import ast
import json
import subprocess
from globals import Globals


class FileUtil:
    @staticmethod
    def read_json(file_path):
        with open(file_path, 'r', encoding="utf-8") as f:
            res = json.load(f)
        return res

    @staticmethod
    def read_file_as_string(file_path):
        with open(file_path, 'r', encoding="utf-8") as f:
            res = f.read()
        return res

    @staticmethod
    def write_file(file_path, content):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

    @staticmethod
    def write_json(file_path, content):
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=4)


class ProcessUtil:
    @staticmethod
    def run_process(cmd, cwd, shell=False):
        if shell:
            print(f"Running {cmd}.")
        else:
            print(f"Running {' '.join(cmd)}.")
        process = subprocess.Popen(cmd, shell=shell, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
        output, errors = process.communicate()
        if process.returncode != 0:
            print("Error:", errors.decode())
            # raise Exception
        else:
            pass
            # print("Output:", output.decode())
        return process.returncode, output

    @staticmethod
    def run_bash_cmd(bash_str, cwd):
        cmd = ["bash", "-c", bash_str]
        return ProcessUtil.run_process(cmd, cwd)


class DataUtil:
    @staticmethod
    def load_data():
        return FileUtil.read_json(Globals.METADATA_PATH)

    @staticmethod
    def snake_to_camel(snake_str):
        words = re.split(r'_', snake_str)
        camel_case = ''.join(word[0].upper() + word[1:] for word in words if word)
        return camel_case

    @staticmethod
    def extract_function_from_file(file_path, func_name):
        file_content = FileUtil.read_file_as_string(file_path)
        # Parse the file content into an AST
        tree = ast.parse(file_content)

        # Find the function definition
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == func_name:
                start_lineno = node.lineno - 1  # Lines in ast are 1-indexed
                end_lineno = node.end_lineno  # End line (only available in Python 3.8+)
                method_lines = file_content.splitlines()[start_lineno:end_lineno]
                method_code = '\n'.join(method_lines)
                return method_code
        return None

    # ========== Methods For Extract 'Oracle' Dependencies ==========
    @staticmethod
    def extract_class_definition(file_path, class_name):
        file_content = FileUtil.read_file_as_string(file_path)
        tree = ast.parse(file_content)

        class ClassVisitor(ast.NodeVisitor):
            def __init__(self):
                self.class_code_list = []
                self.current_scope = None

            def visit_Assign(self, node):
                if self.current_scope == class_name:
                    self.class_code_list += file_content.splitlines()[node.lineno-1:node.end_lineno]

            def visit_AnnAssign(self, node):
                if self.current_scope == class_name:
                    self.class_code_list += file_content.splitlines()[node.lineno-1:node.end_lineno]

            def visit_FunctionDef(self, node):
                if self.current_scope == class_name and node.name == '__init__':
                    self.class_code_list += file_content.splitlines()[node.lineno-1:node.end_lineno]

            def visit_ClassDef(self, node):
                if node.name == class_name:
                    previous_scope = self.current_scope
                    self.current_scope = node.name
                    # add the class signature
                    self.class_code_list += file_content.splitlines()[node.lineno-1:node.lineno]
                    self.generic_visit(node)
                    self.current_scope = previous_scope

        visitor = ClassVisitor()
        visitor.visit(tree)
        return '\n'.join(visitor.class_code_list)

    @staticmethod
    def extract_method_from_class(file_path, class_name, method_name):
        file_content = FileUtil.read_file_as_string(file_path)
        tree = ast.parse(file_content)

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == class_name:
                for item in node.body:
                    if isinstance(item, ast.FunctionDef) and item.name == method_name:
                        code_lines = file_content.splitlines()[item.lineno-1:item.end_lineno]
                        return '\n'.join(code_lines)
        return None

    @staticmethod
    def extract_variable_from_file(file_path, var_name):
        class VarVisitor(ast.NodeVisitor):
            def __init__(self):
                self.var_code_list = []
                self.current_scope = None

            def visit_Assign(self, node):
                if self.current_scope is None:
                    for target in node.targets:
                        if isinstance(target, ast.Name) and target.id == var_name:
                            code_lines = file_content.splitlines()[node.lineno-1:node.end_lineno]
                            self.var_code_list += code_lines

            def visit_AnnAssign(self, node):
                if self.current_scope is None:
                    for target in node.targets:
                        if isinstance(target, ast.Name) and target.id == var_name:
                            code_lines = file_content.splitlines()[node.lineno-1:node.end_lineno]
                            self.var_code_list += code_lines

            def visit_FunctionDef(self, node):
                # Set a different scope for function definitions
                previous_scope = self.current_scope
                self.current_scope = node
                self.generic_visit(node)
                self.current_scope = previous_scope  # Restore previous scope

            def visit_ClassDef(self, node):
                # Set a different scope for class definitions
                previous_scope = self.current_scope
                self.current_scope = node
                self.generic_visit(node)
                self.current_scope = previous_scope  # Restore previous scope

        file_content = FileUtil.read_file_as_string(file_path)
        tree = ast.parse(file_content)
        visitor = VarVisitor()
        visitor.visit(tree)
        return '\n'.join(visitor.var_code_list)

    @staticmethod
    def extract_imports_from_file(file_path, package_name):
        class ImportVisitor(ast.NodeVisitor):
            def __init__(self):
                self.imports = []
                self.current_scope = None

            def visit_Import(self, node):
                if self.current_scope is None:
                    for alias in node.names:
                        if package_name == alias.name:
                            self.imports.append(ast.unparse(node))

            def visit_ImportFrom(self, node):
                if self.current_scope is None:
                    if package_name == node.module:
                        self.imports.append(ast.unparse(node))

            def visit_FunctionDef(self, node):
                # Set a different scope for function definitions
                previous_scope = self.current_scope
                self.current_scope = node
                self.generic_visit(node)
                self.current_scope = previous_scope  # Restore previous scope

            def visit_ClassDef(self, node):
                # Set a different scope for class definitions
                previous_scope = self.current_scope
                self.current_scope = node
                self.generic_visit(node)
                self.current_scope = previous_scope  # Restore previous scope

        file_content = FileUtil.read_file_as_string(file_path)
        tree = ast.parse(file_content)
        visitor = ImportVisitor()
        visitor.visit(tree)
        return visitor.imports


    @staticmethod
    def get_leading_spaces(string):
        return len(string) - len(string.lstrip())

    @staticmethod
    def remove_leading_spaces(string):
        lines = string.splitlines()
        leading_space = DataUtil.get_leading_spaces(lines[0])
        return '\n'.join(l[leading_space:] for l in lines)

    @staticmethod
    def extract_function_from_output(output, func_name):
        code_list = output.split('\n')
        # prune the infinitely generated code such as '# ...\n' by GPT-3.5
        # if len(code_list) > 100:
        #     code_list = code_list[:100]
        method_code_list = []
        is_this_method = False
        leading_space = 0
        method_def_prefix = 'def ' + func_name + '('
        for i, line in enumerate(code_list):
            if method_def_prefix in line:
                is_this_method = True
                leading_space = DataUtil.get_leading_spaces(line)
                method_code_list.append(line[leading_space:])
            elif is_this_method:
                if (DataUtil.get_leading_spaces(line) > leading_space
                        or len(line) == 0 or all(char.isspace() for char in line)):
                    method_code_list.append(line[leading_space:])
                else:
                    break
        method_code = '\n'.join(method_code_list)
        return method_code

    @staticmethod
    def replace_method_in_code(code, method_name, method_code):
        code_list = code.split('\n')
        method_code_list = method_code.split('\n')
        target_code_list = []
        method_def_prefix = "def " + method_name + '('
        leading_space = 0
        is_this_method = False
        for line in code_list:
            if method_def_prefix in line:
                is_this_method = True
                leading_space = DataUtil.get_leading_spaces(line)
            elif is_this_method:
                if DataUtil.get_leading_spaces(line) > leading_space or len(line) == 0 or line == '\r':
                    continue
                else:
                    is_this_method = False
                    for method_line in method_code_list:
                        target_code_list.append(' ' * leading_space + method_line)
                    target_code_list.append('')  # add a blank line before next method
                    target_code_list.append(line)
            else:
                target_code_list.append(line)
        # replace the last method
        if is_this_method:
            for method_line in method_code_list:
                target_code_list.append(' ' * leading_space + method_line)
        return '\n'.join(target_code_list)

    @staticmethod
    def replace_method_in_code_for_infile_prompt(code, method_name, method_code):
        # match multiline signature
        pattern = re.compile(rf"\n?\s*def\s+{method_name}\s*\([^)]*?\)[^:]*?:[^\n]*?\n", re.DOTALL)
        matched = pattern.search(code)
        span = matched.span()

        context_above = code[:span[0]]
        context_below = code[span[1]:]
        method_def_prefix = 'def ' + method_name + '('
        leading_space = 0
        for line in code.split('\n'):
            if method_def_prefix in line:
                leading_space = DataUtil.get_leading_spaces(line)
                break
        # add replaced code
        context_below_list = method_code.split('\n')
        is_this_method = True
        for line in context_below.split('\n'):
            if is_this_method and (DataUtil.get_leading_spaces(line) > leading_space
                                   or len(line) == 0 or all(char.isspace() for char in line)):
                continue
            else:
                is_this_method = False
                # concat the context below the target function
                context_below_list.append(line)
        method_code = (DataUtil.handle_extremely_long_field(context_above, 8192, False) + '\n\n' +
                       DataUtil.handle_extremely_long_field('\n'.join(context_below_list)))
        return method_code

    @staticmethod
    def handle_extremely_long_field(text, max_length=8192, cut_from_tail=True):
        """
        Truncate extremely long fields in the prompt.
        :param text: str, text to be truncate.
        :param tokenizer: Tokenizer, a specified tokenizer for the used model.
        :param max_length: int, the max length of the field.
        :param cut_from_tail: bool, cut from the tail of the input text if True.
        :return: str, truncated text if it is over-length.
        """
        tokenizer = tiktoken.get_encoding('cl100k_base')
        tokens = tokenizer.encode_ordinary(text)
        if len(tokens) > max_length:
            if cut_from_tail:
                return tokenizer.decode(tokens[:max_length])
            else:
                return tokenizer.decode(tokens[-max_length:])
        else:
            return text


class PathUtil:
    @staticmethod
    def get_name_string(model_str, task_mode, dep_mode, temperature):
        temp_str = str(int(temperature * 10))
        if task_mode == 1:
            return f"{model_str}_Task_{dep_mode}_temp{temp_str}"
        return f"{model_str}_{dep_mode}_temp{temp_str}"

    @staticmethod
    def get_log_output_path(name_string):
        log_dir = os.path.join(Globals.RESULT_PATH, 'log')
        os.makedirs(log_dir, exist_ok=True)
        return os.path.join(log_dir, f"{name_string}_log_output.log")

    @staticmethod
    def get_output_path(name_string):
        output_dir = os.path.join(Globals.RESULT_PATH, 'output')
        os.makedirs(output_dir, exist_ok=True)
        return os.path.join(output_dir, f"{name_string}_output.json")

    @staticmethod
    def get_tmp_output_path(name_string, tmp_idx, method_name):
        tmp_output_dir = os.path.join(Globals.RESULT_PATH, 'tmp_output')
        os.makedirs(tmp_output_dir, exist_ok=True)
        return os.path.join(tmp_output_dir, f"{name_string}_tmp_{tmp_idx}_{method_name}_output.json")

    @staticmethod
    def get_test_output_path(name_string):
        test_output_dir = os.path.join(Globals.RESULT_PATH, 'test')
        os.makedirs(test_output_dir, exist_ok=True)
        return os.path.join(test_output_dir, f"{name_string}_test_output.json")

    @staticmethod
    def get_tmp_test_file_output_path():
        tmp_test_dir = os.path.join(Globals.RESULT_PATH, 'tmp_test')
        os.makedirs(tmp_test_dir, exist_ok=True)
        return tmp_test_dir

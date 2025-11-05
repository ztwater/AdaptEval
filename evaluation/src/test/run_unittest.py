import os.path
import sys
import importlib
import unittest
import argparse
from func_timeout import func_set_timeout
from func_timeout.exceptions import FunctionTimedOut
from src.utils import FileUtil, PathUtil


@func_set_timeout(5)  # set timeout to 5 seconds
def run_unittest(test_path, test_module_name, test_class_name, name_string):
    sys.path.append(test_path)
    # print(sys.path)
    log_path = PathUtil.get_log_output_path(name_string)
    with open(log_path, 'a', encoding='utf-8') as f:
        test_module = importlib.import_module(test_module_name)
        test_class = getattr(test_module, test_class_name)
        test_suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_result = unittest.TextTestRunner(stream=f).run(test_suite)
    return test_result


def parse_unittest_result(test_path, test_module_name, test_class_name, name_string):
    res_item = {}
    try:
        res = run_unittest(test_path, test_module_name, test_class_name, name_string)
        res_item['compilation'] = 'success'
        res_item['errors'] = get_error_log(res.errors)
        res_item['failures'] = get_error_log(res.failures)
        res_item['total_run'] = res.testsRun
    # catch the timeout exception
    except FunctionTimedOut as timeout:
        print(timeout)
        res_item['compilation'] = 'success'
        res_item['errors'] = {'TimeoutError': {}}
        res_item['failures'] = {}
        res_item['total_run'] = 0
    except Exception as e:
        print(e)
        res_item['compilation'] = str(e)
        res_item['errors'] = {}
        res_item['failures'] = {}
        res_item['total_run'] = 0
    return res_item


def get_error_log(failed_tests):
    error_dict = {}
    for failed_test in failed_tests:
        test_id, stacktrace = failed_test
        current_test_name = str(test_id).split(' ')[0]
        stacks = stacktrace.split('\n')
        error_output = ''
        for stack in stacks:
            # get the line with 'XXXError:'
            if 'Error:' in stack:
                error_output = stack
                break
        # error_output = stacktrace.split('\n')[-2]  # get the last line of the stacktrace
        error_type, error_info = error_output.split('Error:')
        error_type += 'Error'
        error_info = error_info.strip()
        if error_type not in error_dict:
            error_dict[error_type] = {}
        error_dict[error_type][current_test_name] = error_info
    return error_dict


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo_id', type=int)
    parser.add_argument('--test_path', type=str)
    parser.add_argument('--test_module_name', type=str)
    parser.add_argument('--test_class_name', type=str)
    parser.add_argument('--name_string', type=str)
    parser.add_argument('--repeat', type=int)
    args = parser.parse_args()
    result_item = parse_unittest_result(args.test_path, args.test_module_name, args.test_class_name, args.name_string)
    tmp_test_path = PathUtil.get_tmp_test_file_output_path()
    tmp_test_res = os.path.join(tmp_test_path, f"{args.repo_id}_{args.test_module_name}_{args.repeat}.json")
    FileUtil.write_json(tmp_test_res, result_item)

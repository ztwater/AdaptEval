import argparse
import os.path
import re

from utils import DataUtil

def replace_pyvenv_cfg(virtual_env_path, home_path, version):
    with open(os.path.join(virtual_env_path, 'pyvenv.cfg'), 'r') as f:
        text = f.read()
    text = re.sub('/home/user/anaconda3/bin', home_path, text)
    text = re.sub('3.11.7', version, text)
    text = re.sub('3.11', '.'.join(version.split('.')[:2]), text)
    text = re.sub('/home/user/AdaptEval', virtual_env_path, text)
    with open(os.path.join(virtual_env_path, 'pyvenv.cfg', 'w')) as f:
        f.write(text)


def replace_virtual_env(virtual_env_path):
    for name in ['activate', 'activate.csh', 'activate.fish']:
        with open(os.path.join(virtual_env_path, 'bin', name), 'r') as f:
            text = f.read()
            text = re.sub('/home/user/AdaptEval', virtual_env_path, text)
        with open(os.path.join(virtual_env_path, name, 'w')) as f:
            f.write(text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--python_home", type=str, help='home of the system python path, e.g., /home/user/anaconda3/bin')
    parser.add_argument("--python_version", type=str, help='python version, e.g., 3.11.7')
    parser.add_argument("--dataset_root", type=str, help='root path of the AdaptEval, e.g., /home/user/AdaptEval')
    args = parser.parse_args()

    for repo_data in DataUtil.load_data():
        repo_id = repo_data['id']
        repo_name = repo_data['repo_name'].split('/')[-1]
        virtual_env_path = str(os.path.join(args.dataset_root, 'benchmark', str(repo_id), repo_name, 'venv'))
        replace_pyvenv_cfg(virtual_env_path, args.python_home, args.python_version)
        replace_virtual_env(virtual_env_path)
        break

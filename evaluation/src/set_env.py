import os

from utils import DataUtil, ProcessUtil
from globals import Globals


def install_env_files():
    install_script_path = os.path.abspath('install_env.sh')
    for repo_data in DataUtil.load_data():
        repo_id = int(repo_data['id'])
        repo_name = repo_data['repo_name'].split('/')[1]
        repo_path = os.path.join(Globals.DATASET_PATH, str(repo_id), str(repo_name))
        if repo_id == 76:  # this repository should install deps individually
            pass
        else:
            ProcessUtil.run_process([install_script_path], repo_path)

if __name__ == '__main__':
    install_env_files()

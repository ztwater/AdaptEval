import os

def create_dir(directory):
    if not os.path.exists(directory):
        print('Creating Directory '+directory)
        os.makedirs(directory)

create_dir('Project directory')

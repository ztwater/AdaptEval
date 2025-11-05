import os
directory = 'mydirpath'

number_of_files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])

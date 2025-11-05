import os
isfile = os.path.isfile
join = os.path.join

directory = 'mydirpath'
number_of_files = sum(1 for item in os.listdir(directory) if isfile(join(directory, item)))

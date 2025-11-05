$ python my_program.py --my_bool False
False

$ python my_program.py --my_bool True
True

$ python my_program.py --my_bool true
usage: my_program.py [-h] [--my_bool {False,True}]
my_program.py: error: argument --my_bool: invalid choice: 'true' (choose from 'False', 'True')

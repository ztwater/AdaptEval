from distutils.util import strtobool

def user_yes_no_query(question):
    sys.stdout.write('%s [y/n]\n' % question)
    while True:
        try:
            return strtobool(raw_input().lower())
        except ValueError:
            sys.stdout.write('Please respond with \'y\' or \'n\'.\n')

#usage

>>> user_yes_no_query('Do you like cheese?')
Do you like cheese? [y/n]
Only on tuesdays
Please respond with 'y' or 'n'.
ok
Please respond with 'y' or 'n'.
y
>>> True

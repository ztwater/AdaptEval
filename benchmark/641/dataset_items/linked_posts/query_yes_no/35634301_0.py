#pip install prompter

from prompter import yesno

>>> yesno('Really?')
Really? [Y/n]
True

>>> yesno('Really?')
Really? [Y/n] no
False

>>> yesno('Really?', default='no')
Really? [y/N]
True

$ ./argparse_example.py one two --bar=three --mod1-foo=11231 --mod2.foo=46546
Namespace(arg1='one', arg2='two', bar='three', foo=0, mod1=Namespace(foo=11231), mod2=Namespace(foo=46546))
three
11231

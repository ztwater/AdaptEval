def foo(*args):
     return [x for x in args if x > 9000] or 'No number over 9000!'

foo(9004, 1, 2, 500)
# [9004]

foo(1, 2, 3, 4)
# 'No number over 9000!'

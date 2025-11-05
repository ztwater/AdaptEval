from dotmap import DotMap

m = DotMap()
m.hello = 'world'
m.hello
m.hello += '!'
# m.hello and m['hello'] now both return 'world!'
m.val = 5
m.val2 = 'Sam'

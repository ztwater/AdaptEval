import re
t = re.compile("[a-zA-Z0-9.,_-]")
unsafe = "abc∂éåß®∆˚˙©¬ñ√ƒµ©∆∫ø"
safe = [ch for ch in unsafe if t.match(ch)]
# => 'abc'

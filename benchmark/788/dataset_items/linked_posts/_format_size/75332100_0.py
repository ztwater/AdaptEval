to_human = lambda v : str(v >> ((max(v.bit_length()-1, 0)//10)*10)) +["", "K", "M", "G", "T", "P", "E"][max(v.bit_length()-1, 0)//10]
>>> to_human(1024)
'1K'
>>> to_human(1024*1024*3)
'3M'

[int(x) if x.replace('-','', 1).replace('+','',1).isdecimal() else float('nan') for x in lst]

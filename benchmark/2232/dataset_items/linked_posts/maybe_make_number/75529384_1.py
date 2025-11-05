[int(x) if x.replace('-','', 1).replace('+','',1).isdecimal() else int(e[0])*10**int(e[1]) if (e:=x.split('e',1))[1:] and e[1].isdecimal() else float('nan') for x in lst]

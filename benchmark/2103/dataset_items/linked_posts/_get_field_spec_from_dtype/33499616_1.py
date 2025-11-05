[(x,str(y[0])) for x,y in sorted(yourArray.dtype.fields.items(),key=lambda k: k[1])]

dups={}

for key,val in dct.iteritems():
    if val.get('alias') != None:
        ref = "%s%s%s" % (val['dst'] , val['src'] ,val['alias'])# a simple hash
        dups.setdefault(ref,[]) 
        dups[ref].append(key)

for k,v in dups.iteritems():
    if len(v) > 1:
        for key in v:
            del dct[key]

def _clean(value):
    return urllib.quote(unicode(value))

'&'.join([ v for val in [[ "%s[%s]=%s"%(k,ik, _(iv)) 
    for ik, iv in v.items()] if type(v)==dict else ["%s=%s"%(k,_(v))] 
    for k,v in data.items() ] 
    for v in val ])

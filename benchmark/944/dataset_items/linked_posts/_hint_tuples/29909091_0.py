import simplejson

def _to_json(python_object) :
    if isinstance(python_object, tuple) :
        python_object = {'__class__': 'tuple',
                         '__value__': list(python_object)}
    else :
        raise TypeError(repr(python_object) + ' is not JSON serializable') 

    return python_object

def _from_json(json_object):                                   
    if json_object['__class__'] == 'tuple':
        return tuple(json_object['__value__'])
    return json_object


jsn = simplejson.dumps((1,2,3), 
                       default=_to_json, 
                       tuple_as_array=False)

tpl = simplejson.loads(jsn, object_hook=_from_json)

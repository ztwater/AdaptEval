    # Pavel Anossov's solution hinted this:
    
    import json
    tuple_signifier = '__tuple__s_i_g_n_i_f_i_e_r__'
    
    class StreamTuple(dict):
         def __hash__(self):
             return hash(str(self))
    
    class MultiDimensionalArrayEncoder(json.JSONEncoder):
        def encode(self, obj):
            def hint_tuples(item, dict_key=False):
                global tuple_signifier
                ret_val = None
                if isinstance(item, tuple):
                    if dict_key:
                        ret_val = json.dumps(dict(
                            [(
                                tuple_signifier,
                                json.dumps(hint_tuples(list(item))),
                            ),],
                        ))
                    else:
                        ret_val = dict(
                            [(
                                tuple_signifier,
                                json.dumps(hint_tuples(list(item))),
                            ),],
                        )
    
                elif isinstance(item, list):
                    ret_val = [hint_tuples(e) for e in item]
                elif isinstance(item, dict):
                    ret_val = dict([
                        (hint_tuples(key, dict_key=True), hint_tuples(value))
                        for key, value in item.items()
                    ])
                else:
                    ret_val = item
                return ret_val
            return super(MultiDimensionalArrayEncoder, self).\
                         encode(hint_tuples(obj))
    
    
    def hinted_tuple_hook(obj):
        global tuple_signifier
    
        ret_val = {}
        if tuple_signifier in obj:
            ret_val = tuple(json.loads(obj[tuple_signifier], object_hook=hinted_tuple_hook,))
        else:
            for k, v in obj.items():
                inner_k = k
                inner_v = v
                if isinstance(k, str) and tuple_signifier in k:
                    inner_k = json.loads(k, object_hook=hinted_tuple_hook,)
                if isinstance(v, str) and tuple_signifier in v:
                    inner_v = json.loads(v, object_hook=hinted_tuple_hook,)
                ret_val[inner_k] = inner_v
        return ret_val
    
    #
    # Some tests that show how to use the above hinted tuple hook to encode 
    # / decode Python tuples.
    #
    if __name__ == '__main__':
        enc = MultiDimensionalArrayEncoder()
        test_input_1 = (2,)
        test_input_2 = {(2,): 'a'}
        test_input_3 = {'a': {(2,): {1:'a'}}}
        print('test_input_1 encoded:', enc.encode(test_input_1), test_input_1)
        print('test_input_1 decoded:',
            json.loads(enc.encode(test_input_1),
                object_hook=hinted_tuple_hook,)
        )
    #"""
        print('test_input_2 encoded:', enc.encode(test_input_2))
        print('test_input_2 decoded:',
            json.loads(enc.encode(test_input_2),
                object_hook=hinted_tuple_hook,)
        )
    
        print('\n' * 3)
        print('test_input_3 encoded:', enc.encode(test_input_3))
        print('test_input_3 decoded:',
            json.loads(enc.encode(test_input_3),
                object_hook=hinted_tuple_hook,)
        )
    
        print('\n' * 3)
        test_input_4 = {'a': 'b'}
        print('test_input_4  encoded:', enc.encode(test_input_4))
        print('test_input_4 decoded:',
            json.loads(enc.encode(test_input_4),
                object_hook=hinted_tuple_hook,)
        )
    
        #"""

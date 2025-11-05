class DotDictMeta(type):                                                          
    def __new__(                                                                  
        cls,                                                                      
        name,                                                                     
        bases,                                                                    
        attrs,                                         
        rename_method=lambda n: f'__{n}__',                            
        **custom_methods,                                                         
    ):                                                                            
        d = dict                                                                  
        attrs.update(                                                             
            cls.get_hidden_or_renamed_methods(rename_method),           
            __getattr__=d.__getitem__,                                            
            __setattr__=d.__setitem__,                                            
            __delattr__=d.__delitem__,                                            
            **custom_methods,                                                     
        )                                                                         
        return super().__new__(cls, name, bases, attrs)                           
                                                                                  
    def __init__(self, name, bases, attrs, **_):                                  
        super().__init__(name, bases, attrs)                                      
                                                                                  
    @property                                                                     
    def attribute_error(self):                                                    
        raise AttributeError                                                      
                                                                                  
    @classmethod                                                                  
    def get_hidden_or_renamed_methods(cls, rename_method=None):                  
        public_methods = tuple(                                                   
            i for i in dict.__dict__.items() if not i[0].startswith('__')         
        )                                                                         
        error = cls.attribute_error                                               
        hidden_methods = ((k, error) for k, v in public_methods)                  
        yield from hidden_methods                                                 
        if rename_method:                                                       
            renamed_methods = ((rename_method(k), v) for k, v in public_methods) 
            yield from renamed_methods                                             
                                                                                  
                                                                                  
class DotDict(dict, metaclass=DotDictMeta):                                       
    pass  

                                                                    
                                                                              

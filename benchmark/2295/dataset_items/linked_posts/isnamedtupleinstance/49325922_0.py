def isinstance_namedtuple(x):                                                               
  return (isinstance(x, tuple) and                                                  
          isinstance(getattr(x, '__dict__', None), collections.Mapping) and         
          getattr(x, '_fields', None) is not None)                                  

def gen_dict_extract(var_0, var_1):
   for key in var_1:
      if hasattr(var_0, 'items'):
         for k, v in var_0.items():
            if k == key:
               yield v
            if isinstance(v, dict):
               for result in gen_dict_extract([key], v):
                  yield result
            elif isinstance(v, list):
               for d in v:
                  for result in gen_dict_extract([key], d):
                     yield result    

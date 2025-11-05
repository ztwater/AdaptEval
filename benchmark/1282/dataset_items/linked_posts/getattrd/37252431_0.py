def multi_getattr(self,obj, attr, default = None):
          attributes = attr.split(".")
          for i in attributes:
              try:
                  obj = getattr(obj, i)
              except AttributeError:
                  if default:
                      return default
                  else:
                      raise
          return obj

def get_class_from_tablename(tablename):
  for c in Base.__subclasses__():
    if c.__tablename__ == tablename:
      return c

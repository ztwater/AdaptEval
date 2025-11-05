def get_class_from_tablename(var_0):
  for c in Base.registry._class_registry.data.values():
    if hasattr(c, '__tablename__') and c.__tablename__ == var_0:
      return c

def get_class_from_tablename(tablename):
  for c in Base.registry._class_registry.data.values():
    if hasattr(c, '__tablename__') and c.__tablename__ == tablename:
      return c

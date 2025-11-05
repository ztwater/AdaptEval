def get_class_by_tablename(tablename, Base):
  for c in Base._decl_class_registry.values():
    if c.__table__.name == tablename:
      return c

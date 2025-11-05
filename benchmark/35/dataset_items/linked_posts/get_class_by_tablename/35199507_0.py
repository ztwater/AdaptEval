def get_class_by_tablename(table_fullname):
  """Return class reference mapped to table.

  :param table_fullname: String with fullname of table.
  :return: Class reference or None.
  """
  for c in Base._decl_class_registry.values():
    if hasattr(c, '__table__') and c.__table__.fullname == table_fullname:
      return c

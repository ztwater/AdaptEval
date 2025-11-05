def get_class_by_table_name(table_name):
    tbl = Base.metadata.tables[table_name]
    return tbl.decl_class

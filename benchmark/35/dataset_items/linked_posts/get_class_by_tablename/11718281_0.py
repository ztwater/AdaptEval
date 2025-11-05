def getModelFromTableName(sTable):
    """
    return the Model class with the given __tablename__
    """
    globals = globals()
    for k in globals:
        if type(globals[k]) == sqlalchemy.ext.declarative.DeclarativeMeta:
            try:
                if globals[k].__tablename__ == sTable:
                    return globals[k]
            except:
                pass
    return None

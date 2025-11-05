from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def get_class_by_tablename(tablename):
    """Return class reference mapped to table.
    https://stackoverflow.com/a/23754464

    :param tablename: String with name of table.
    :return: Class reference or None.
    """
    # for c in Base.registry._class_registry.data.values():
    for c in db.Model._decl_class_registry.values():
        if hasattr(c, "__tablename__") and c.__tablename__ == tablename:
            return c
    return None


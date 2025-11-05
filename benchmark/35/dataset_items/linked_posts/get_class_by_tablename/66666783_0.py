Base.TBLNAME_TO_CLASS = {}

for mapper in Base.registry.mappers:
    cls = mapper.class_
    classname = cls.__name__
    if not classname.startswith('_'):
        tblname = cls.__tablename__
        Base.TBLNAME_TO_CLASS[tblname] = cls

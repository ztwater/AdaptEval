# Python 3.7.2 Console
>>> from app import models as m
>>> account_table = m.Base.metadata.tables['account']
>>> account_table.__class__
<class 'sqlalchemy.sql.schema.Table'>

>>> account_table.decl_class
<class 'app.models.Account'>

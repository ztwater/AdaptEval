>>> from pydoc import locate
>>> locate('int')
<type 'int'>
>>> t = locate('int')
>>> t('1')
1

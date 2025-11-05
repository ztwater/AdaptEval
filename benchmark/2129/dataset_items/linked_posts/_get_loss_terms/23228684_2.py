>>> inspect.signature(foo)
<inspect.Signature object at 0x100bda588>
>>> str(inspect.signature(foo))
"(bar:str, baz:list, spam:str='eggs', *, monty:str='python', **kw) -> None"
>>> inspect.signature(foo).parameters
mappingproxy(OrderedDict([('bar', <Parameter at 0x100bd67c8 'bar'>), ('baz', <Parameter at 0x100bd6ea8 'baz'>), ('spam', <Parameter at 0x100bd69f8 'spam'>), ('monty', <Parameter at 0x100bd6c28 'monty'>), ('kw', <Parameter at 0x100bd6548 'kw'>)]))


In [1]: from minydra import MinyDict

In [2]: args = MinyDict({"foo": "bar", "yes.no.maybe": "idontknow"}).pretty_print(); args
╭──────────────────────────────╮
│ foo          : bar           │
│ yes.no.maybe : idontknow     │
╰──────────────────────────────╯
Out[2]: {'foo': 'bar', 'yes.no.maybe': 'idontknow'}

In [3]: args.resolve().pretty_print(); args
╭──────────────────────────╮
│ foo : bar                │
│ yes                      │
│ │no                      │
│ │ │maybe : idontknow     │
╰──────────────────────────╯
Out[3]: {'foo': 'bar', 'yes': {'no': {'maybe': 'idontknow'}}}

In [4]: args.yes.no.maybe
Out[4]: "idontknow"

In [5]: "foo" in args
Out[5]: True

In [6]: "rick" in args
Out[6]: False

In [7]: args.morty is None
Out[7]: True

In [8]: args.items()
Out[8]: dict_items([('foo', 'bar'), ('yes', {'no': {'maybe': 'idontknow'}})])

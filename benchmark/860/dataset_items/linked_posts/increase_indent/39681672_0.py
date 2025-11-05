import yaml

class MyDumper(yaml.Dumper):

    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)

foo = {
    'name': 'foo',
    'my_list': [
        {'foo': 'test', 'bar': 'test2'},
        {'foo': 'test3', 'bar': 'test4'}],
    'hello': 'world',
}

print yaml.dump(foo, Dumper=MyDumper, default_flow_style=False)

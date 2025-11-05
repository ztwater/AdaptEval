class Nestedspace(argparse.Namespace):
    def __setattr__(self, name, value):
        if '.' in name:
            group,name = name.split('.',1)
            ns = getattr(self, group, Nestedspace())
            setattr(ns, name, value)
            self.__dict__[group] = ns
        else:
            self.__dict__[name] = value

p = argparse.ArgumentParser()
p.add_argument('--foo')
p.add_argument('--bar', dest='test.bar')
print(p.parse_args('--foo test --bar baz'.split()))

ns = Nestedspace()
print(p.parse_args('--foo test --bar baz'.split(), ns))
p.add_argument('--deep', dest='test.doo.deep')
args = p.parse_args('--foo test --bar baz --deep doodod'.split(), Nestedspace())
print(args)
print(args.test.doo)
print(args.test.doo.deep)

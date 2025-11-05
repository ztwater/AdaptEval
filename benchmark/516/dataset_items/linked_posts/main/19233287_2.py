def str2bool(v):
  #susendberg's function
  return v.lower() in ("yes", "true", "t", "1")
p = argparse.ArgumentParser()
p.register('type','bool',str2bool) # add type keyword to registries
p.add_argument('-b',type='bool')  # do not use 'type=bool'
# p.add_argument('-b',type=str2bool) # works just as well
p.parse_args('-b false'.split())
Namespace(b=False)

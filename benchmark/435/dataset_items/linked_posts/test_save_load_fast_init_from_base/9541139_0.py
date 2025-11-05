 >>> class A(object):
...    ARG=1
... 
 >>> a = A()
 >>> A().ARG
 1
 >>> b = A()
 >>> b.ARG
 1
 >>> a.ARG=2
 >>> b.ARG
 1

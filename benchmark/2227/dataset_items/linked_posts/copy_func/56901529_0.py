import pickle
import dill
import types

def foo():
    print ('a')


oldCode=foo.__code__

name='IAmFooCopied'

newCode= types.CodeType(
        oldCode.co_argcount,             #   integer
        oldCode.co_kwonlyargcount,       #   integer
        oldCode.co_nlocals,              #   integer
        oldCode.co_stacksize,            #   integer
        oldCode.co_flags,                #   integer
        oldCode.co_code,                 #   bytes
        oldCode.co_consts,               #   tuple
        oldCode.co_names,                #   tuple
        oldCode.co_varnames,             #   tuple
        oldCode.co_filename,             #   string
        name,                  #   string
        oldCode.co_firstlineno,          #   integer
        oldCode.co_lnotab,               #   bytes
        oldCode.co_freevars,             #   tuple
        oldCode.co_cellvars              #   tuple
        )

IAmFooCopied=types.FunctionType(newCode, foo.__globals__, name,foo.__defaults__ , foo.__closure__)
IAmFooCopied.__qualname__= name
print ( 'printing foo and the copy', IAmFooCopied, foo )
print ( 'dill output: ', dill.dumps(IAmFooCopied ))
print ( 'pickle Output: ', pickle.dumps (IAmFooCopied) )

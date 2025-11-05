from timeit import timeit

from dotwiz import DotWiz
from dotmap import DotMap


d = {'hey': {'so': [{'this': {'is': {'pretty': {'cool': True}}}}]}}

dw = DotWiz(d)
# ✫(hey=✫(so=[✫(this=✫(is=✫(pretty={'cool'})))]))

dm = DotMap(d)
# DotMap(hey=DotMap(so=[DotMap(this=DotMap(is=DotMap(pretty={'cool'})))]))

assert dw.hey.so[0].this['is'].pretty.cool == dm.hey.so[0].this['is'].pretty.cool

n = 100_000

print('dotwiz (create):  ', round(timeit('DotWiz(d)', number=n, globals=globals()), 3))
print('dotmap (create):  ', round(timeit('DotMap(d)', number=n, globals=globals()), 3))
print('dotwiz (get):  ', round(timeit("dw.hey.so[0].this['is'].pretty.cool", number=n, globals=globals()), 3))
print('dotmap (get):  ', round(timeit("dm.hey.so[0].this['is'].pretty.cool", number=n, globals=globals()), 3))

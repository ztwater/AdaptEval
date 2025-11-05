#!/usr/bin/python3
# coding=utf-8
"""
Natural-Sort Test
"""

from re import compile, split

dre = compile(r'(\d+)')
mylist = ['elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13', 'elm']
mylist2 = ['e0lm', 'e1lm', 'E2lm', 'e9lm', 'e10lm', 'E12lm', 'e13lm', 'elm', 'e01lm']

mylist.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in split(dre, l)])
mylist2.sort(key=lambda l: [int(s) if s.isdigit() else s.lower() for s in split(dre, l)])

print(mylist)  
  # ['elm', 'elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13']
print(mylist2)  
  # ['e0lm', 'e1lm', 'e01lm', 'E2lm', 'e9lm', 'e10lm', 'E12lm', 'e13lm', 'elm']

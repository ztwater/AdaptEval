#! /usr/bin/python3
import sys
import re
if len(sys.argv)!=2:
     exit("Syntax:python3 exe18.py inputfile.cc ")
else:
     print ('The following files are given by you:',sys.argv[0],sys.argv[1])
with open(sys.argv[1],'r') as ifile:
    newstring=re.sub(r'/\*.*?\*/',' ',ifile.read(),flags=re.S)
with open(sys.argv[1],'w') as ifile:
    ifile.write(newstring)
print('/* */ have been removed from the inputfile')
with open(sys.argv[1],'r') as ifile:
      newstring1=re.sub(r'//.*',' ',ifile.read())
with open(sys.argv[1],'w') as ifile:
      ifile.write(newstring1)
print('// have been removed from the inputfile')

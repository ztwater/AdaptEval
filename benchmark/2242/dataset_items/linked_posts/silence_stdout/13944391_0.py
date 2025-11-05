#!/usr/bin/python
import os
import sys
import datetime

ITER = 10000000
def printlots(out, it, st="abcdefghijklmnopqrstuvwxyz1234567890"):
   temp = sys.stdout
   sys.stdout = out
   i = 0
   start_t = datetime.datetime.now()
   while i < it:
      print st
      i = i+1
   end_t = datetime.datetime.now()
   sys.stdout = temp
   print out, "\n   took", end_t - start_t, "for", it, "iterations"

class devnull():
   def write(*args):
      pass


printlots(open(os.devnull, 'wb'), ITER)
printlots(devnull(), ITER)

#!/usr/bin/python

from appscript import *
import argparse

def __main__():
  parser = argparse.ArgumentParser(description='Set desktop wallpaper.')
  parser.add_argument('file', type=file, help='File to use as wallpaper.')
  args = parser.parse_args()
  f = args.file
  se = app('System Events')
  desktops = se.desktops.display_name.get()
  for d in desktops:
    desk = se.desktops[its.display_name == d]
    desk.picture.set(mactypes.File(f.name))


__main__()

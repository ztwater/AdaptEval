import os,sys,inspect
import pathlib

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
your_folder = currentdir + "/" + "your_folder"

if not os.path.exists(your_folder):
   pathlib.Path(your_folder).mkdir(parents=True, exist_ok=True)

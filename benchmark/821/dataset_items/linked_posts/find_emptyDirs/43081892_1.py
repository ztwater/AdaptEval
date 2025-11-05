gdsfile  = "/home/hha/temp.gds"
try:
   open(gdsfile, 'x')
except FileExistsError:
   pass

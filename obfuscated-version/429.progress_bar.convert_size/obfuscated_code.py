import math

def convert_size(var_0):
   if var_0 == 0:
       return "0B"
   var_1 = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   var_2 = int(math.floor(math.log(var_0, 1024)))
   var_3 = math.pow(1024, var_2)
   var_4 = round(var_0 / var_3, 2)
   return "%s %s" % (var_4, var_1[var_2])

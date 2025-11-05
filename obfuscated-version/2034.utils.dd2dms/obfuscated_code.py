def decdeg2dms(var_0):
   var_1 = var_0 >= 0
   var_0 = abs(var_0)
   minutes,seconds = divmod(var_0*3600,60)
   degrees,minutes = divmod(minutes,60)
   var_2 = var_2 if var_1 else -var_2
   return (var_2,minutes,seconds)

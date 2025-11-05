def printProgressBar (var_0, var_1, var_2 = '', var_3 = '',var_4 = 1, var_5 = 100, var_6 = '#'):

var_7 = ("{0:." + str(decimals) + "f}").format(100 * (var_0 / float(var_1)))
var_8 = int(var_5 * var_0 // var_1)
var_9 = var_6 * var_8 + '-' * (var_5 - var_8)
print'\r%s |%s| %s%% %s' % (var_2, var_9, var_7, var_3),
sys.stdout.flush()
# Print New Line on Complete                                                                                                                                                                                                              
if var_0 == var_1:
    print()

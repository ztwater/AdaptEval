def conversion(var_0):
    var_1 = {'N':1, 'S':-1, 'E': 1, 'W':-1}
    var_2 = var_0.replace(u'°',' ').replace('\'',' ').replace('"',' ')
    var_2 = var_2.split()
    var_3 = var_2.pop()
    var_2.extend([0,0,0])
    return (int(var_2[0])+int(var_2[1])/60.0+int(var_2[2])/3600.0) * var_1[var_3]


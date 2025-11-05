>>> un_camel = lambda i: i[0].lower() + str.join('', ("_" + c.lower() if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" else c for c in i[1:]))
>>> un_camel("camel_case")
'camel_case'
>>> un_camel("CamelCase")
'camel_case'

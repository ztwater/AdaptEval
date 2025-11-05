>>> def un_camel(input):
...     output = [input[0].lower()]
...     for c in input[1:]:
...             if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
...                     output.append('_')
...                     output.append(c.lower())
...             else:
...                     output.append(c)
...     return str.join('', output)
...
>>> un_camel("camel_case")
'camel_case'
>>> un_camel("CamelCase")
'camel_case'

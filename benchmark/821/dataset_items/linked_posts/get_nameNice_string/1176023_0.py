import re

name = 'CamelCaseName'
name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
print(name)  # camel_case_name

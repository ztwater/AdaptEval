>>> re.sub('(?!^)([A-Z]+)', r'_\1','CamelCase').lower()
'camel_case'
>>> re.sub('(?!^)([A-Z]+)', r'_\1','CamelCamelCase').lower()
'camel_camel_case'
>>> re.sub('(?!^)([A-Z]+)', r'_\1','Camel2Camel2Case').lower()
'camel2_camel2_case'
>>> re.sub('(?!^)([A-Z]+)', r'_\1','getHTTPResponseCode').lower()
'get_httpresponse_code'

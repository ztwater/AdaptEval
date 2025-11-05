>>> re.sub('([A-Z]+)', r'_\1','CamelCase').lower()
'_camel_case'  
>>> re.sub('([A-Z]+)', r'_\1','camelCase').lower()
'camel_case'
>>> re.sub('([A-Z]+)', r'_\1','camel2Case2').lower()
'camel2_case2'
>>> re.sub('([A-Z]+)', r'_\1','camelCamelCase').lower()
'camel_camel_case'
>>> re.sub('([A-Z]+)', r'_\1','getHTTPResponseCode').lower()
'get_httpresponse_code'

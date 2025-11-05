>>> a = re.compile('((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))')
>>> a.sub(r'_\1', 'getHTTPResponseCode').lower()
'get_http_response_code'
>>> a.sub(r'_\1', 'get2HTTPResponseCode').lower()
'get2_http_response_code'
>>> a.sub(r'_\1', 'get2HTTPResponse123Code').lower()
'get2_http_response123_code'
>>> a.sub(r'_\1', 'HTTPResponseCode').lower()
'http_response_code'
>>> a.sub(r'_\1', 'HTTPResponseCodeXYZ').lower()
'http_response_code_xyz'

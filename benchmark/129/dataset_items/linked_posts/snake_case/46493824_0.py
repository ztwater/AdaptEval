import re

def convert (camel_input):
    words = re.findall(r'[A-Z]?[a-z]+|[A-Z]{2,}(?=[A-Z][a-z]|\d|\W|$)|\d+', camel_input)
    return '_'.join(map(str.lower, words))


# Let's test it
test_strings = [
    'CamelCase',
    'camelCamelCase',
    'Camel2Camel2Case',
    'getHTTPResponseCode',
    'get200HTTPResponseCode',
    'getHTTP200ResponseCode',
    'HTTPResponseCode',
    'ResponseHTTP',
    'ResponseHTTP2',
    'Fun?!awesome',
    'Fun?!Awesome',
    '10CoolDudes',
    '20coolDudes'
]
for test_string in test_strings:
    print(convert(test_string))

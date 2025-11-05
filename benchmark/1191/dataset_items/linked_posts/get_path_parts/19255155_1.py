import re    
var = "/var/stuff/morestuff/furtherdown/THEFILE.txt"
result = re.split( r'[\\/]', var )
filter( None, result )
['var', 'stuff', 'morestuff', 'furtherdown', 'THEFILE.txt']

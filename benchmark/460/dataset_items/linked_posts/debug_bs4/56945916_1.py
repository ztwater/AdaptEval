Diagnostic running on Beautiful Soup 4.7.1
Python version 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]]
Found lxml version 4.3.3.0
Found html5lib version 1.0.1

Trying to parse your markup with html.parser
Here's what html.parser did with the markup:
<?xml version="1.0" encoding="ISO-8859-15"?>
<sometag>
</sometag>
--------------------------------------------------------------------------------
Trying to parse your markup with html5lib
Here's what html5lib did with the markup:
<!--?xml version="1.0" encoding="ISO-8859-15"?-->
<html>
 <head>
 </head>
 <body>
  <sometag>
  </sometag>
 </body>
</html>
--------------------------------------------------------------------------------
Trying to parse your markup with lxml
Here's what lxml did with the markup:
<?xml version="1.0" encoding="ISO-8859-15"?>
<html>
 <body>
  <sometag>
  </sometag>
 </body>
</html>
--------------------------------------------------------------------------------
Trying to parse your markup with lxml-xml
Here's what lxml-xml did with the markup:
<?xml version="1.0" encoding="utf-8"?>

--------------------------------------------------------------------------------

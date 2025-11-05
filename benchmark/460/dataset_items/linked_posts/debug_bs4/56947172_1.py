Diagnostic running on Beautiful Soup 4.7.1
Python version 3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 13:35:33) [MSC v.1900 64 bit (AMD64)]
I noticed that html5lib is not installed. Installing it may help.
Found lxml version 4.3.4.0
Trying to parse your markup with html.parser
Here's what html.parser did with the markup:
<?xml version="1.0" encoding="ISO-8859-15"?>
<sometag>
</sometag>
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
<someTag>
</someTag>
--------------------------------------------------------------------------------

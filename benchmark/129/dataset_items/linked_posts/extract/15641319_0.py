import re

xmlstring = re.sub(' xmlns="[^"]+"', '', xmlstring, count=1)

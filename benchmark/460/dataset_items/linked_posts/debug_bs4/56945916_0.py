from bs4 import BeautifulSoup

from bs4.diagnose import diagnose

with open('iso-8859-15_example.xml', encoding="iso-8859-15") as f:
    diagnose(f.read())

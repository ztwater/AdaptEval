from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
with open('iso-8859-15_example.xml', 'rb') as f:
    diagnose(f)

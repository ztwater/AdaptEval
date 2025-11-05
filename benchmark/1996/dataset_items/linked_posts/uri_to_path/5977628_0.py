import os
from urllib.parse import urlparse
p = urlparse('file://C:/test/doc.txt')
final_path = os.path.abspath(os.path.join(p.netloc, p.path))

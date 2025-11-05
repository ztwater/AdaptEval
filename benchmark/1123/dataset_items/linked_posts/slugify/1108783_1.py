from random import choice
from string import ascii_lowercase, ascii_uppercase, digits
allowed_chr = ascii_lowercase + ascii_uppercase + digits

safe = ''.join([choice(allowed_chr) for _ in range(16)])
# => 'CYQ4JDKE9JfcRzAZ'

import string
for chr in your_string:
 if chr == ' ':
   your_string = your_string.replace(' ', '_')
 elif chr not in string.ascii_letters or chr not in string.digits:
    your_string = your_string.replace(chr, '')

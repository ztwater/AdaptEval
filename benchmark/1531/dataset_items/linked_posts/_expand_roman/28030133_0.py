import re
s = 0;
a = dict();
b = dict();
r = "MMCMXCVIII"

a['CM'] = 900;
a['IX'] = 9;
a ['IV'] = 4;
a ['XL'] = 40;
a ['CD'] = 400;
a ['XC'] = 90;

b['M'] = 1000;
b['C'] = 100;
b['D'] = 500;
b['X'] = 10;
b['V'] = 5;
b['L'] = 50;
b['I'] = 1;

# Handle the tricky 4's and 9's first and remove them from the string

for key in a:
        if key in r: 
            r = re.sub(key,'',r)
            s+=a[key];
# Then straightforward multiplication of the not-so-tricky ones by their count.

for key in b:
         s+= r.count(key) * b[key];

print s; # This will print 2998

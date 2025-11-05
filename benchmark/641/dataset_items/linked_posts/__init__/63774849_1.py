import re
regex = re.compile("^M{0,4}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$")
matchArray = regex.match("MMMCMXCIX")

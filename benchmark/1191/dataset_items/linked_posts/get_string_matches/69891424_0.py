import re
my_strings = ['SetVariables "a" "b" "c" ', 'd2efw   f "first" +&%#$%"second",vwrfhir, d2e   u"third" dwedew', '"uno"?>P>MNUIHUH~!@#$%^&*()_+=0trewq"due"        "tre"fef    fre f', '       "uno""dos"      "tres"', '"unu""doua""trei"', '      "um"                    "dois"           "tres"                  ']
my_substrings = []
for current_test_string in my_strings:
    for values in re.findall(r'\"(.+?)\"', current_test_string):
        my_substrings.append(values)
        #print("values are:",values,"=")
    print(" my_substrings are:",my_substrings,"=")
    my_substrings = []

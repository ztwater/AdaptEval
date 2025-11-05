template_b = "The current name is {name.upper() * 2}"
for name in names:
    print(fstr(template_b))
# The current name is FOOFOO
# The current name is BARBAR

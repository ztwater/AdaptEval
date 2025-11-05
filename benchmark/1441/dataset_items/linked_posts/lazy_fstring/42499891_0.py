def template_a():
    return f"The current name is {name}"

names = ["foo", "bar"]
for name in names:
    print(template_a())

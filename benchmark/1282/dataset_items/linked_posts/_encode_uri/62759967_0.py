import re
text = "hello ,world!"
replaces = {"hello": "hi", "world":" 2020", "!":"."}
regex = re.sub("|".join(replaces.keys()), lambda match: replaces[match.string[match.start():match.end()]], text)
print(regex)

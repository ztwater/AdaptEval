import re
import ast


def doit(text):
    matches=re.findall(r'"(?:(?:(?!(?<!\\)").)*)"',text)
    for match in matches:
        print(match, '=>', ast.literal_eval(match))


doit('Regex should return "String 1" or "String 2" or "String3" and "\\"double quoted string\\"" ')

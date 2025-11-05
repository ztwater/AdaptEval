import re
r=r"'(\\'|[^'])*(?!<\\)'|\"(\\\"|[^\"])*(?!<\\)\""

texts=[r'"aerrrt"',
r'"a\"e'+"'"+'rrt"',
r'"a""""arrtt"""""',
r'"aerrrt',
r'"a\"errt'+"'",
r"'aerrrt'",
r"'a\'e"+'"'+"rrt'",
r"'a''''arrtt'''''",
r"'aerrrt",
r"'a\'errt"+'"',
      "''",'""',""]

for text in texts:
     print (text,"-->",re.fullmatch(r,text))

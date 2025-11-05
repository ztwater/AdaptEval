def doit(text):      
  import re
  matches = re.findall(r'"(.+?)"',text)
  # matches is now ['String 1', 'String 2', 'String3']
  return ",".join(matches)

doit('Regex should return "String 1" or "String 2" or "String3" ')

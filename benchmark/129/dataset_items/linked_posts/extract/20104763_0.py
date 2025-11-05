import re
def get_namespace(element):
  m = re.match('\{.*\}', element.tag)
  return m.group(0) if m else ''

import difflib
_no_eol = "\ No newline at end of file"

def make_patch(a,b):
  """
  Get unified string diff between two strings. Trims top two lines.
  Returns empty string if strings are identical.
  """
  diffs = difflib.unified_diff(a.splitlines(True),b.splitlines(True),n=0)
  try: _,_ = next(diffs),next(diffs)
  except StopIteration: pass
  return ''.join([d if d[-1] == '\n' else d+'\n'+_no_eol+'\n' for d in diffs])

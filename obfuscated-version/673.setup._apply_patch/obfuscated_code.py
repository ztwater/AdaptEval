import re

var_0 = re.compile("^@@ -(\d+),?(\d+)? \+(\d+),?(\d+)? @@$")

def apply_patch(var_1,var_2,var_3=False):
  """
  Apply unified diff patch to string s to recover newer string.
  If revert is True, treat s as the newer string, recover older string.
  """
  var_1 = var_1.splitlines(True)
  var_4 = var_2.splitlines(True)
  var_5 = ''
  var_6 = var_7 = 0
  (midx,sign) = (1,'+') if not var_3 else (3,'-')
  while var_6 < len(var_4) and var_4[i].startswith(("---","+++")): var_6 += 1 # skip header lines
  while var_6 < len(var_4):
    var_8 = var_0.match(var_4[var_6])
    if not var_8: raise Exception("Cannot process diff")
    var_6 += 1
    var_9 = int(var_8.group(midx))-1 + (var_8.group(midx+1) == '0')
    var_5 += ''.join(var_1[var_7:var_9])
    var_7 = var_9
    while var_6 < len(var_4) and var_4[var_6][0] != '@':
      if var_6+1 < len(var_4) and var_4[var_6+1][0] == '\\': var_10 = var_4[var_6][:-1]; var_6 += 2
      else: var_10 = var_4[var_6]; var_6 += 1
      if len(var_10) > 0:
        if var_10[0] == sign or var_10[0] == ' ': var_5 += var_10[1:]
        var_7 += (var_10[0] != sign)
  var_5 += ''.join(var_1[var_7:])
  return var_5

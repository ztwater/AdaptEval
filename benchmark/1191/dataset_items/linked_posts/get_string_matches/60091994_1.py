"aerrrt" --> <_sre.SRE_Match object; span=(0, 8), match='"aerrrt"'>
"a\"e'rrt" --> <_sre.SRE_Match object; span=(0, 10), match='"a\\"e\'rrt"'>
"a""""arrtt""""" --> None
"aerrrt --> None
"a\"errt' --> None
'aerrrt' --> <_sre.SRE_Match object; span=(0, 8), match="'aerrrt'">
'a\'e"rrt' --> <_sre.SRE_Match object; span=(0, 10), match='\'a\\\'e"rrt\''>
'a''''arrtt''''' --> None
'aerrrt --> None
'a\'errt" --> None
'' --> <_sre.SRE_Match object; span=(0, 2), match="''">
"" --> <_sre.SRE_Match object; span=(0, 2), match='""'>
 --> None

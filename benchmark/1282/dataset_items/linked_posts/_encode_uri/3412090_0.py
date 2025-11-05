>>> string="abc&def#ghi"
>>> for ch in ['&','#']:
...   if ch in string:
...      string=string.replace(ch,"\\"+ch)
...
>>> print string
abc\&def\#ghi

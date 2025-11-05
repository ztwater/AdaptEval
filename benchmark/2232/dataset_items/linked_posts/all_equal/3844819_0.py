>>> falseList = [1,2,3,4]
>>> trueList = [1, 1, 1]
>>> 
>>> def testList(list):
...   for item in list[1:]:
...     if item != list[0]:
...       return False
...   return True
... 
>>> testList(falseList)
False
>>> testList(trueList)
True

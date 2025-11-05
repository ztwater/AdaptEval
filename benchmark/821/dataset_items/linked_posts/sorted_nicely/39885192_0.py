def alphaNumOrder(string):
   """ Returns all numbers on 5 digits to let sort the string with numeric order.
   Ex: alphaNumOrder("a6b12.125")  ==> "a00006b00012.00125"
   """
   return ''.join([format(int(x), '05d') if x.isdigit()
                   else x for x in re.split(r'(\d+)', string)])

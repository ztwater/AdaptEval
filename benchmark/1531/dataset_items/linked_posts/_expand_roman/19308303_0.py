def numberOfNumeral(n):
    """ Return the number represented by the single numeral """
    # e.g. "v" -> 5, "i" -> 5 (and handle v/V cases, etc.)

# avoid "string" as a variable name
# I chose "ns" for "numerals" (which might be better),
# but I'm also a bit terse .. anyway, name variables for what they represents.
ns = str(input("Enter a roman numeral"))

while ns:
   firstNum = numberOfNumeral(ns[0])
   # This makes secondValue = -1 when there is only one numeral left
   # so firstNum is always "at least" secondNum when len(ns) == 1. 
   secondNum = numberOfNumeral(ns[1]) if len(ns) > 1 else -1
   if firstNum is at least secondNum:
      # Add firstNum to total.
      # Remove the character - so that the loop state advances.
      # If we don't don't his, as in the original, it will never end.
      # Here we use "slice notation".
      ns = ns[1:] 
   else:
      # Add the difference, secondNum - firstNum, to total.
      # Remove both characters - again, so we advance state.
      ns = ns[2:]

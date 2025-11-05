lzt = [1,1,1,1,1,2]

if (len(set(lzt)) > 1):
    uniform = False
elif (len(set(lzt)) == 1):
    uniform = True
elif (not lzt):
    raise ValueError("List empty, get wrecked")

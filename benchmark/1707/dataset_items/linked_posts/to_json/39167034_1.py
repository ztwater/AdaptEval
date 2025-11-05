try:
    val = a.property
except AttributeError:
    otherStuff()
else:
    doStuff(val)

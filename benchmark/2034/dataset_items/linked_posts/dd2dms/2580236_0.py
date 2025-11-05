def decdeg2dms(dd):
    mult = -1 if dd < 0 else 1
    mnt,sec = divmod(abs(dd)*3600, 60)
    deg,mnt = divmod(mnt, 60)
    return mult*deg, mult*mnt, mult*sec

dd = 45 + 30/60 + 1/3600
print(decdeg2dms(dd))

# negative value returns all negative elements
print(decdeg2dms(-122.442))

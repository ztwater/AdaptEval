# recreate `newstr` from `oldstr`+patch
newstr = apply_patch(oldstr, diffstr)
# recreate `oldstr` from `newstr`+patch
oldstr = apply_patch(newstr, diffstr, True)

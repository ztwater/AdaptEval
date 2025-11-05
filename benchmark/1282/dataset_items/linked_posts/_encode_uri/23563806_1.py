strs, replacements = "abc&def#ghi", {"&": "\&", "#": "\#"}
print "".join([replacements.get(c, c) for c in strs])
# abc\&def\#ghi

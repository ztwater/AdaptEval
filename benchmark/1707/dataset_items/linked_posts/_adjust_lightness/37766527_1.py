c = Color((51, 153, 255))
# c = Color((0.5, 0.1, 0.8), fmt='rgb0') # It should work with rgb0
# c = Color('#05d4fa', fmt='hex')        # and hex but I don't remember if it was well tested so be careful (the conversions might be messy).
c._testPalette(1)
print(c.rgbColors)

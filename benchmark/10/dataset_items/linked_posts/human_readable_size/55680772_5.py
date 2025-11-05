>>> abbreviate(999_994)
'999.99K'
>>> abbreviate(999_995)
'1M'
>>> abbreviate(999_995, precision=3)
'999.995K'
>>> abbreviate(2042, base=1024)
'1.99K'
>>> abbreviate(2043, base=1024)
'2K'

>>> pretty_size(42)
'42 B'

>>> pretty_size(2015)
'2.0 KiB'

>>> pretty_size(987654321)
'941.9 MiB'

>>> pretty_size(9876543210)
'9.2 GiB'

>>> pretty_size(0.5,pow=1)
'512 B'

>>> pretty_size(0)
'0 B'

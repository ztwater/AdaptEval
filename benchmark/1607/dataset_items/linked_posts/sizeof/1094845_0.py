>>> from hurry.filesize import alternative
>>> size(1, system=alternative)
'1 byte'

>>> size(10, system=alternative)
'10 bytes'

>>> size(1024, system=alternative)
'1 KB'

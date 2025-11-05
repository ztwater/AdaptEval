utf-8     'ABC'
utf-8-sig '\xef\xbb\xbfABC'
utf-16    '\xff\xfeA\x00B\x00C\x00'    # Adds BOM and encodes using native processor endian-ness.
utf-16le  'A\x00B\x00C\x00'
utf-16be  '\x00A\x00B\x00C'

utf-8  w/ BOM decoded with utf-8     u'\ufeffABC'    # doesn't remove BOM if present.
utf-8  w/ BOM decoded with utf-8-sig u'ABC'          # removes BOM if present.
utf-16 w/ BOM decoded with utf-16    u'ABC'          # *requires* BOM to be present.
utf-16 w/ BOM decoded with utf-16le  u'\ufeffABC'    # doesn't remove BOM if present.

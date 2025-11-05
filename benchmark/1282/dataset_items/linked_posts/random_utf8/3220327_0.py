>>> t = u'𝐟𝐨𝐨'
>>> e = t.encode('utf-16le')
>>> ''.join(unichr(x).encode('utf-8') for x in struct.unpack('<' + 'H' * (len(e) // 2), e))
'\xed\xa0\xb5\xed\xb0\x9f\xed\xa0\xb5\xed\xb0\xa8\xed\xa0\xb5\xed\xb0\xa8'

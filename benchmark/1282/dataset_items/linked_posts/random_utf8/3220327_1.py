mysql> create table utf8test (t character(128)) collate utf8_general_ci;
Query OK, 0 rows affected (0.12 sec)

  ...

>>> cxn = MySQLdb.connect(..., charset='utf8')
>>> csr = cxn.cursor()
>>> t = u'𝐟𝐨𝐨'
>>> e = t.encode('utf-16le')
>>> v = ''.join(unichr(x).encode('utf-8') for x in struct.unpack('<' + 'H' * (len(e) // 2), e))
>>> v
'\xed\xa0\xb5\xed\xb0\x9f\xed\xa0\xb5\xed\xb0\xa8\xed\xa0\xb5\xed\xb0\xa8'
>>> csr.execute('insert into utf8test (t) values (%s)', (v,))
1L
>>> csr.execute('select * from utf8test')
1L
>>> r = csr.fetchone()
>>> r
(u'\ud835\udc1f\ud835\udc28\ud835\udc28',)
>>> print r[0]
𝐟𝐨𝐨

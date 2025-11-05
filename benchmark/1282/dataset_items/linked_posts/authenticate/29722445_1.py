Traceback (most recent call last):
  File "ldap_ssl.py", line 28, in <module>
    ld.start_tls_s()
  File "/Library/Python/2.7/site-packages/python_ldap-2.4.19-py2.7-macosx-10.10-intel.egg/ldap/ldapobject.py", line 571, in start_tls_s
    return self._ldap_call(self._l.start_tls_s)
  File "/Library/Python/2.7/site-packages/python_ldap-2.4.19-py2.7-macosx-10.10-intel.egg/ldap/ldapobject.py", line 106, in _ldap_call
    result = func(*args,**kwargs)
ldap.CONNECT_ERROR: {'info': 'error:14090086:SSL routines:SSL3_GET_SERVER_CERTIFICATE:certificate verify failed (unable to get local issuer certificate)', 'desc': 'Connect error'}

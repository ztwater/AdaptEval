[_ldap]
library_dirs = /usr/local/opt/openldap/lib /usr/lib /usr/local/lib
include_dirs = /usr/local/opt/openldap/include /usr/include/sasl /usr/include /usr/local/include
extra_compile_args = -g -arch x86_64
extra_objects = 
libs = ldap_r lber sasl2 ssl crypto

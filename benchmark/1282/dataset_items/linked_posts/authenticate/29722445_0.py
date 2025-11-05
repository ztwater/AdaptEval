# Force libldap to create a new SSL context (must be last TLS option!)
ld.set_option(ldap.OPT_X_TLS_NEWCTX, 0)

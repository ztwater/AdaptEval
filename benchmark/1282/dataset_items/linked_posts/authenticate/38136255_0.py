    try:
        self.ld = ldap.initialize(self.ldap_host)
        if self.configuration['verify_ssl']['verify']:
            self.ld.set_option(ldap.OPT_X_TLS_CACERTFILE, self.configuration['verify_ssl']['use'])
        else:
            self.ld.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
        self.ld.ldap.set_option(ldap.OPT_X_TLS_NEWCTX, 0)

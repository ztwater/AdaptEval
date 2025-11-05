class WhitelistRemoteAddrFix(object):
    """This middleware can be applied to add HTTP proxy support to an
    application that was not designed with HTTP proxies in mind.  It
    only sets `REMOTE_ADDR` from `X-Forwarded` headers.

    Tests proxies against a set of trusted proxies.

    The original value of `REMOTE_ADDR` is stored in the WSGI environment
    as `werkzeug.whitelist_remoteaddr_fix.orig_remote_addr`.

    :param app: the WSGI application
    :param trusted_proxies: a set or sequence of proxy ip addresses that can be trusted.
    """

    def __init__(self, app, trusted_proxies=()):
        self.app = app
        self.trusted_proxies = frozenset(trusted_proxies)

    def get_remote_addr(self, remote_addr, forwarded_for):
        """Selects the new remote addr from the given list of ips in
        X-Forwarded-For.  Picks first non-trusted ip address.
        """

        if remote_addr in self.trusted_proxies:
            return next((ip for ip in reversed(forwarded_for)
                         if ip not in self.trusted_proxies),
                        remote_addr)

    def __call__(self, environ, start_response):
        getter = environ.get
        remote_addr = getter('REMOTE_ADDR')
        forwarded_for = getter('HTTP_X_FORWARDED_FOR', '').split(',')
        environ.update({
            'werkzeug.whitelist_remoteaddr_fix.orig_remote_addr': remote_addr,
        })
        forwarded_for = [x for x in [x.strip() for x in forwarded_for] if x]
        remote_addr = self.get_remote_addr(remote_addr, forwarded_for)
        if remote_addr is not None:
            environ['REMOTE_ADDR'] = remote_addr
        return self.app(environ, start_response)

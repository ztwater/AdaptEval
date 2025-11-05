class ResourceProxy(object):
    def __init__(self):
        self._resource = Resource()

    def __getattr__(self, key):
        return getattr(self._resource, key)

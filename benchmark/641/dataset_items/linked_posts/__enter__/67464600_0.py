class Resource(object):
    ...
    def __enter__(self):
        return self
            
    def __exit__(self, *exc):
        self.close()

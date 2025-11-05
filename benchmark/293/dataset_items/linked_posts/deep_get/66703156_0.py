class new_dict(dict):
    def deep_get(self, *args, default=None):
        _empty_dict = {}
        out = self
        for key in args:
            out = out.get(key, _empty_dict)
        return out if out else default

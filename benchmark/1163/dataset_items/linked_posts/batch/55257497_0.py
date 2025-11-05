class DotDict(dict):

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def __getattr__(self, key):

        def typer(candidate):
            if isinstance(candidate, dict):
                return DotDict(candidate)

            if isinstance(candidate, str):  # iterable but no need to iter
                return candidate

            try:  # other iterable are processed as list
                return [typer(item) for item in candidate]
            except TypeError:
                return candidate

            return candidate

        return typer(dict.get(self, key))

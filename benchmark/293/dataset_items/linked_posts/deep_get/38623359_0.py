from functools import reduce # Python 3
def deepgetitem(obj, item, fallback=None):
    """Steps through an item chain to get the ultimate value.

    If ultimate value or path to value does not exist, does not raise
    an exception and instead returns `fallback`.

    >>> d = {'snl_final': {'about': {'_icsd': {'icsd_id': 1}}}}
    >>> deepgetitem(d, 'snl_final.about._icsd.icsd_id')
    1
    >>> deepgetitem(d, 'snl_final.about._sandbox.sbx_id')
    >>>
    """
    def getitem(obj, name):
        try:
            return obj[name]
        except (KeyError, TypeError):
            return fallback
    return reduce(getitem, item.split('.'), obj)

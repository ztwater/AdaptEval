class DotNotation(dict):
    
    __setattr__= dict.__setitem__
    __delattr__= dict.__delitem__

    def __init__(self, data):
        if isinstance(data, str):
            data = json.loads(data)
    
        for name, value in data.items():
            setattr(self, name, self._wrap(value))

    def __getattr__(self, attr):
        def _traverse(obj, attr):
            if self._is_indexable(obj):
                try:
                    return obj[int(attr)]
                except:
                    return None
            elif isinstance(obj, dict):
                return obj.get(attr, None)
            else:
                return attr
        if '.' in attr:
            return reduce(_traverse, attr.split('.'), self)
        return self.get(attr, None)

    def _wrap(self, value):
        if self._is_indexable(value):
            # (!) recursive (!)
            return type(value)([self._wrap(v) for v in value])
        elif isinstance(value, dict):
            return DotNotation(value)
        else:
            return value
    
    @staticmethod
    def _is_indexable(obj):
        return isinstance(obj, (tuple, list, set, frozenset))


if __name__ == "__main__":
    test_dict = {
        "dimensions": {
            "length": "112",
            "width": "103",
            "height": "42"
        },
        "meta_data": [
            {
                "id": 11089769,
                "key": "imported_gallery_files",
                "value": [
                    "https://example.com/wp-content/uploads/2019/09/unnamed-3.jpg",
                    "https://example.com/wp-content/uploads/2019/09/unnamed-2.jpg",
                    "https://example.com/wp-content/uploads/2019/09/unnamed-4.jpg"
                ]
            }
        ]
    }
    dotted_dict = DotNotation(test_dict)
    print(dotted_dict.dimensions.length) # => '112'
    print(getattr(dotted_dict, 'dimensions.length')) # => '112'
    print(dotted_dict.meta_data[0].key) # => 'imported_gallery_files'
    print(getattr(dotted_dict, 'meta_data.0.key')) # => 'imported_gallery_files'
    print(dotted_dict.meta_data[0].value) # => ['link1','link2','link2']
    print(getattr(dotted_dict, 'meta_data.0.value')) # => ['link1','link2','link3']
    print(dotted_dict.meta_data[0].value[2]) # => 'link3'
    print(getattr(dotted_dict, 'meta_data.0.value.2')) # => 'link3'

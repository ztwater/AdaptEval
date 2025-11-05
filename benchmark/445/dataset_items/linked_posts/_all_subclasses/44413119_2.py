def get_subclasses(cls):

    def _subclasses(classes, seen):
        subclasses = sum(*(frozenset(x.__subclasses__()) for x in classes))
        found = classes + seen
        if not subclasses:
            return found

        return _subclasses(subclasses, found)

    return _subclasses([cls], [])

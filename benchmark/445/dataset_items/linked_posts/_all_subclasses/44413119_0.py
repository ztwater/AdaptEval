def get_subclasses_gen(cls):

    def _subclasses(classes, seen):
        while True:
            subclasses = sum((x.__subclasses__() for x in classes), [])
            yield from classes
            yield from seen
            found = []
            if not subclasses:
                return

            classes = subclasses
            seen = found

    return _subclasses([cls], [])

def descendents(cls):
    '''Does not return the class itself'''
    R = {}
    def visit(cls):
        for subCls in cls.__subclasses__():
            if not subCls in R:
                R[subCls] = True
                visit(subCls)
    visit(cls)
    return list(R.keys())

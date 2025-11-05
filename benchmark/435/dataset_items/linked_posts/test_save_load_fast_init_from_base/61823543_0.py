def copy_class(c,name=None):
    if not name: name = 'CopyOf'+c.__name__
    if hasattr(c,'__slots__'):
        slots = c.__slots__ if type(c.__slots__) != str else (c.__slots__,)
        dict_ = dict()
        sloted_members = dict()
        for k,v in c.__dict__.items():
            if k not in slots:
                dict_[k] = v
            elif type(v) != types.MemberDescriptorType:
                sloted_members[k] = v
        CopyOfc = type(name, c.__bases__, dict_)
        for k,v in sloted_members.items():
            setattr(CopyOfc,k,v)
        return CopyOfc
    else:
        dict_ = dict(c.__dict__)
        return type(name, c.__bases__, dict_)

import inspect

def get_object_from(source, path: str):
    """用于进行从module或者其他对象中提取类似 'xxx.yyy.zzz' 路径的对象

    Parameters
    ----------
    source
        源，比如module或class
    path
        待获取的对象路径

    Returns
    -------
    ret
        获取到的对象，或None
    """
    ret = source

    if path == '':
        return ret

    for part in path.split('.'):
        ret = getattr(ret, part, None)
        if ret is None:
            break

    return ret

def get_nest_prefix_by_qualname(obj) -> str:
    """通过解析__qualname__提取对象在模块中的嵌套路径，如果是模块下直接定义的对象，则返回空字符串

    Parameters
    ----------
    obj
        待获取嵌套路径的对象，可以为type、类实例或方法以及其他具有__qualname__的对象

    Returns
    -------
    ret
        如果目标属于某嵌套定义下，则返回__qualname__中提取的嵌套路径（不包含对象本身的名字），
        如果是模块下直接定义的对象，则返回空字符串
    """
    segments = obj.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)
    return '.'.join(segments[:-1])


def get_class_that_defined_method(meth):
    """获取定义指定方法的类

    Parameters
    ----------
    meth
        方法实例

    Returns
    -------
    ret
        定义meth的类，或者None，代表该方法无法找到

    Notes
    -----
        由于Python3移除了所有类和类中定义的方法的直接关联，因此只能通过一些方法来“猜测”，所以理论上存在无法获取到正确结果的情况

        比如如果随意修改__qualname__或者__module__的值会导致结果不可预测

    References
    ----------
        By @Yoel and with assistance from comments

        "Get class from meth.__globals__" patch by @Alexander_McFarlane

        https://stackoverflow.com/questions/3589311/get-defining-class-of-unbound-method-object-in-python-3/

        Modified to support statically nested class using 'get_object_from'
    """
    import functools
    if isinstance(meth, functools.partial):
        return get_class_that_defined_method(meth.func)
    if inspect.ismethod(meth) or (inspect.isbuiltin(meth) and
                                  getattr(meth, '__self__', None) is not None and
                                  getattr(meth.__self__, '__class__', None)):
        for cls in inspect.getmro(meth.__self__.__class__):
            if meth.__name__ in cls.__dict__:
                return cls
        meth = getattr(meth, '__func__', meth)  # fallback to __qualname__ parsing
    if inspect.isfunction(meth):
        class_prefix = get_nest_prefix_by_qualname(meth)
        cls = get_object_from(inspect.getmodule(meth), class_prefix)
        if cls is None:
            path_segs = class_prefix.split('.')
            cls = get_object_from(meth.__globals__.get(path_segs[0]), '.'.join(path_segs))
        if isinstance(cls, type):
            return cls
    return getattr(meth, '__objclass__', None)  # handle special descriptor objects
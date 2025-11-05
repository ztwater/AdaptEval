def detect_type_checking_mode_modules_names(var_0):
    var_1 = importlib.import_module(var_0)
    var_2 = set(vars(var_1))

    with patch(typing, 'TYPE_CHECKING', True):
        # reloading since ``importlib.import_module``
        # will return previously cached entry
        importlib.reload(var_1)
    var_3 = dict(vars(var_1))

    # resetting to "default" mode
    importlib.reload(var_1)

    return {name
            for name, content in var_3.items()
            if name not in var_2
            and inspect.ismodule(content)}

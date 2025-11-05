def detect_type_checking_mode_modules_names(module_name):
    module = importlib.import_module(module_name)
    default_module_names = set(vars(module))

    with patch(typing, 'TYPE_CHECKING', True):
        # reloading since ``importlib.import_module``
        # will return previously cached entry
        importlib.reload(module)
    type_checked_module_namespace = dict(vars(module))

    # resetting to "default" mode
    importlib.reload(module)

    return {name
            for name, content in type_checked_module_namespace.items()
            if name not in default_module_names
            and inspect.ismodule(content)}

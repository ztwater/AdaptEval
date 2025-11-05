for field_name, field_def in self.__dataclass_fields__.items():
    if isinstance(field_def.type, typing._SpecialForm):
        # No check for typing.Any, typing.Union, typing.ClassVar (without parameters)
        continue
    try:
        actual_type = field_def.type.__origin__
    except AttributeError:
        # In case of non-typing types (such as <class 'int'>, for instance)
        actual_type = field_def.type
    # In Python 3.8 one would replace the try/except with
    # actual_type = typing.get_origin(field_def.type) or field_def.type
    if isinstance(actual_type, typing._SpecialForm):
        # case of typing.Union[…] or typing.ClassVar[…]
        actual_type = field_def.type.__args__

    actual_value = getattr(self, field_name)
    if not isinstance(actual_value, actual_type):
        print(f"\t{field_name}: '{type(actual_value)}' instead of '{field_def.type}'")
        ret = False

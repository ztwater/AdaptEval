class BoolAction(Action):
    def __init__(
            self,
            option_strings,
            dest,
            nargs=None,
            default: bool = False,
            **kwargs,
    ):
        if nargs is not None:
            raise ValueError('nargs not allowed')
        super().__init__(option_strings, dest, default=default, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        input_value = values.lower()
        b = input_value in ['true', 'yes', '1']
        if not b and input_value not in ['false', 'no', '0']:
            raise ValueError('Invalid boolean value "%s".)
        setattr(namespace, self.dest, b)

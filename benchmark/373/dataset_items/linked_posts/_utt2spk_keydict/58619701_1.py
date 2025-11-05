class FormatText:
    __slots__ = ['align_list']

    def __init__(self, align_list: list, autoreset=True):
        """
        USAGE::

            format_text = FormatText([(20, '<'), (60, '<')])
            red_dc = format_text.new_dc(fore_color=Fore.RED)
            print(red_dc(['column 1', 'column 2']))
            print(red_dc('good morning'))
        :param align_list:
        :param autoreset:
        """
        self.align_list = align_list
        colorama.init(autoreset=autoreset)

    def __call__(self, text_list: list):
        if len(text_list) != len(self.align_list):
            if isinstance(text_list, str):
                return text_list
            raise AttributeError
        return ' '.join(f'{txt:{flag}{int_align}}' for txt, (int_align, flag) in zip(text_list, self.align_list))

    def new_dc(self, fore_color: Fore = Fore.GREEN, back_color: Back = ""):  # DECORATOR
        """create a device context"""
        def wrap(msgs):
            return back_color + fore_color + self(msgs) + Fore.RESET
        return wrap

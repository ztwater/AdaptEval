import textwrap
from argparse import ArgumentParser, HelpFormatter


def wrap_paragraphs(text: str, width: int, indent: str):
    """
    Wrapper around `textwrap.wrap()` which keeps newlines in the input string
    intact.
    """
    lines = list[str]()

    for i in text.splitlines():
        paragraph_lines = \
            textwrap.wrap(i, width, initial_indent=indent, subsequent_indent=indent)

        # `textwrap.wrap()` will return an empty list when passed an empty
        # string (which happens when there are two consecutive line breaks in
        # the input string). This would lead to those line breaks being
        # collapsed into a single line break, effectively removing empty lines
        # from the input. Thus, we add an empty line in that case.
        lines.extend(paragraph_lines or [''])

    return lines


class Formatter(HelpFormatter):
    def _split_lines(self, text, width):
        return wrap_paragraphs(text, width, '')

    def _fill_text(self, text, width, indent):
        return '\n'.join(wrap_paragraphs(text, width, indent))


parser = ArgumentParser(
    prog='guide',
    formatter_class=Formatter,
    description='The Hitch Hiker\'s Guide to the Galaxy is a wholly remarkable '
                'book. It has been compiled and recompiled many times over '
                'many years and under many different editorships. It contains'
                'contributions from countless numbers of travellers and '
                'researchers.\n'
                '\n'
                'The introduction begins like this:\n'
                '\n'
                '"Space," it says "is big. Really big"\n')

parser.add_argument(
    '--probability',
    help='"But what does it mean?" cried Arthur.\n'
         '"What, the custard?"\n'
         '"No, the measurement of probability!"\n')


parser.print_help()

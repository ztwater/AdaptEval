from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, \ 
                     RawTextHelpFormatter
import textwrap

class CustomArgumentFormatter(ArgumentDefaultsHelpFormatter, RawTextHelpFormatter):
    """Formats argument help which maintains line length restrictions as well as appends default value if present."""

    def _split_lines(self, text, width):
        text = super()._split_lines(text, width)
        new_text = []

        # loop through all the lines to create the correct wrapping for each line segment.
        for line in text:
            if not line:
                # this would be a new line.
                new_text.append(line)
                continue

            # wrap the line's help segment which preserves new lines but ensures line lengths are
            # honored
            new_text.extend(textwrap.wrap(line, width))

        return new_text

class CustomArgumentFormatter(argparse.ArgumentDefaultsHelpFormatter):
    """
    Formats help text to honor newlines and tabs (and show default values).
    """

    # Match multiples of regular spaces only.
    _SPACE_MATCHER = re.compile(r' +', re.ASCII)

    def _split_lines(self, text, width):
        new_text = []
        for line in text.splitlines():
          # For each newline in the help message, replace any multiples of
          # whitespaces (due to indentation in source code) with one space.
          line = self._SPACE_MATCHER.sub(' ', line).rstrip()
          # Fit the line length to the console width
          new_text.extend(textwrap.wrap(line, width))
        return new_text

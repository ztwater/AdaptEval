class RawFormatter(HelpFormatter):
    def _fill_text(self, text, width, indent):
        text = textwrap.dedent(text)          # Strip the indent from the original python definition that plagues most of us.
        text = textwrap.indent(text, indent)  # Apply any requested indent.
        text = text.splitlines()              # Make a list of lines
        text = [textwrap.fill(line, width) for line in text] # Wrap each line 
        text = "\n".join(text)                # Join the lines again
        return text

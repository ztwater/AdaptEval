import argparse
import textwrap

class DescriptionWrappedNewlineFormatter(argparse.HelpFormatter):
    """An argparse formatter that:
    * preserves newlines (like argparse.RawDescriptionHelpFormatter),
    * removes leading indent (great for multiline strings),
    * and applies reasonable text wrapping.

    Source: https://stackoverflow.com/a/64102901/79125
    """
    def _fill_text(self, text, width, indent):
        # Strip the indent from the original python definition that plagues most of us.
        text = textwrap.dedent(text)
        text = textwrap.indent(text, indent)  # Apply any requested indent.
        text = text.splitlines()  # Make a list of lines
        text = [textwrap.fill(line, width) for line in text]  # Wrap each line
        text = "\n".join(text)  # Join the lines again
        return text


class WrappedNewlineFormatter(DescriptionWrappedNewlineFormatter):
    """An argparse formatter that:
    * preserves newlines (like argparse.RawTextHelpFormatter),
    * removes leading indent and applies reasonable text wrapping (like DescriptionWrappedNewlineFormatter),
    * applies to all help text (description, arguments, epilogue).
    """
    def _split_lines(self, text, width):
        # Allow multiline strings to have common leading indentation.
        text = textwrap.dedent(text)
        text = text.splitlines()
        lines = []
        for line in text:
            wrapped_lines = textwrap.fill(line, width).splitlines()
            lines.extend(subline for subline in wrapped_lines)
            if line:
                lines.append("")  # Preserve line breaks.
        return lines


if __name__ == "__main__":
    def demo_formatter(formatter):
        parser = argparse.ArgumentParser(
            description="""
                A program that does things.
                Lots of description that describes how the program works.

                very long lines are wrapped. very long lines are wrapped. very long lines are wrapped. very long lines are wrapped. very long lines are wrapped. very long lines are wrapped.

                existing wrapping will be preserved if within width. existing
                wrapping is preserved. existing wrapping will be preserved.
                existing wrapping is preserved. existing wrapping will be
                preserved. existing wrapping is preserved. existing wrapping
                will be preserved. existing wrapping is preserved unless it goes too long for the display width.
                """,
            formatter_class=formatter,
        )
        parser.add_argument(
            "--option",
            choices=[
                "red",
                "blue",
            ],
            help="""
                Lots of text describing different choices.
                    red: a warning colour
                    text on the next line

                    blue: a longer blah blah keeps going going going going going going going going going going
                """,
        )
        print("\n\nDemo for {}\n".format(formatter.__name__))
        parser.print_help()

    demo_formatter(DescriptionWrappedNewlineFormatter)
    demo_formatter(WrappedNewlineFormatter)

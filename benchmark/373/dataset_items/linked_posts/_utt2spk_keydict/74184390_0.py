import textwrap

class CustomHelpFormatter(argparse.ArgumentDefaultsHelpFormatter):
    def _split_lines(self, text, width):
        wrapper = textwrap.TextWrapper(width=width)
        lines = []
        for line in text.splitlines():
            if len(line) > width:
                lines.extend(wrapper.wrap(line))
            else:
                lines.append(line)
        return lines

parser = argparse.ArgumentParser(formatter_class=CustomArgumentFormatter)

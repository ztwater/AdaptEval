from argparse import HelpFormatter

def lws(line):
    prefix = line[:len(line) - len(line.lstrip())]
    return len(prefix) + 3 * prefix.count('\t')

class SmartHelpFormatter(HelpFormatter):
    def _split_lines(self, text, width):
        r = []
        for line in lines():
            n = lws(line)
            r.extend(' ' * n + s for s in super()._split_lines(line, width - n))
        return r

    def _fill_text(self, text, width, indent):
        r = []
        for line in text.splitlines():
            n = lws(line)
            r.append(super()._fill_text(line, width, indent + ' ' * n))
        return '\n'.join(r)

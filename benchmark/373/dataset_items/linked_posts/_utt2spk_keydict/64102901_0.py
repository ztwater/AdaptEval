#!/usr/bin/python3
import textwrap
from argparse import ArgumentParser, HelpFormatter

class RawFormatter(HelpFormatter):
    def _fill_text(self, text, width, indent):
        return "\n".join([textwrap.fill(line, width) for line in textwrap.indent(textwrap.dedent(text), indent).splitlines()])

program_descripton = f'''
    FunkyTool v1.0

    Created by the Funky Guy on January 1 2020
    Copyright 2020. All rights reserved.

    Licensed under The Hippocratic License 2.1
    https://firstdonoharm.dev/

    Distributed on an "AS IS" basis without warranties
    or conditions of any kind, either express or implied.

    USAGE:
    '''

parser = ArgumentParser(description=program_descripton, formatter_class=RawFormatter)
args = parser.parse_args()

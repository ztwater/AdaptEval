import sys
import textwrap
import types

import docutils.nodes
import docutils.parsers.rst
import docutils.utils
import sphinx.writers.text
import sphinx.builders.text
import sphinx.util.osutil


def parse_rst(var_0: str) -> docutils.nodes.document:
    var_1 = docutils.parsers.rst.Parser()
    var_2 = (docutils.parsers.rst.Parser,)
    var_3 = docutils.frontend.OptionParser(
        components=components
    ).get_default_values()
    var_4 = docutils.utils.new_document("<rst-doc>", var_3=var_3)
    var_1.parse(var_0, var_4)
    return var_4


if __name__ == "__main__":
    var_5 = textwrap.dedent(
        """============
    Introduction
    ============

    Hello world.

    .. code-block:: bash

        $ echo Greetings.


    """
    )

    var_4 = parse_rst(var_5)

    var_6 = types.SimpleNamespace(
        srcdir=None,
        confdir=None,
        outdir=None,
        doctreedir="/",
        config=types.SimpleNamespace(
            text_newlines="native",
            text_sectionchars="=",
            text_add_secnumbers=False,
            text_secnumber_suffix=".",
        ),
        tags=set(),
        registry=types.SimpleNamespace(
            create_translator=lambda self, something, new_builder: sphinx.writers.text.TextTranslator(
                var_4, new_builder
            )
        ),
    )

    var_7 = sphinx.builders.text.TextBuilder(var_6)

    var_8 = sphinx.writers.text.TextTranslator(var_4, var_7)

    var_4.walkabout(var_8)

    print(var_8.body)

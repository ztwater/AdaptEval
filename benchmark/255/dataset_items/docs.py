import types
import warnings
import logging
from typing import cast


def rst2txt(source: str) -> str:
    """
    adapted from https://stackoverflow.com/questions/57119361/convert-restructuredtext-to-plain-text-programmatically-in-python
    """
    try:
        import docutils.nodes
        import docutils.parsers.rst
        import docutils.utils
        import sphinx.writers.text
        import sphinx.builders.text
        import sphinx.util.osutil
        from sphinx.application import Sphinx

        # parser rst
        parser = docutils.parsers.rst.Parser()
        components = (docutils.parsers.rst.Parser,)
        settings = docutils.frontend.OptionParser(
            components=components
        ).get_default_values()
        document = docutils.utils.new_document("<rst-doc>", settings=settings)
        parser.parse(source, document)

        # sphinx
        _app = types.SimpleNamespace(
            srcdir=None,
            confdir=None,
            outdir=None,
            doctreedir="/",
            events=None,
            config=types.SimpleNamespace(
                text_newlines="native",
                text_sectionchars="=",
                text_add_secnumbers=False,
                text_secnumber_suffix=".",
            ),
            tags=set(),
            registry=types.SimpleNamespace(
                create_translator=lambda self, something, new_builder: sphinx.writers.text.TextTranslator(
                    document, new_builder
                )
            ),
        )
        app = cast(Sphinx, _app)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            builder = sphinx.builders.text.TextBuilder(app)
        translator = sphinx.writers.text.TextTranslator(document, builder)
        document.walkabout(translator)
        return str(translator.body)
    except Exception as e:
        logging.warning("Got the following error during rst conversion: %s", e)
        return source

import unicodedata
from random import choice

import perfplot
import regex
import text_unidecode


def remove_accent_chars_regex(x: str):
    return regex.sub(r'\p{Mn}', '', unicodedata.normalize('NFKD', x))


def remove_accent_chars_join(x: str):
    # answer by MiniQuark
    # https://stackoverflow.com/a/517974/7966259
    return u"".join([c for c in unicodedata.normalize('NFKD', x) if not unicodedata.combining(c)])


perfplot.show(
    setup=lambda n: ''.join([choice('Málaga François Phút Hơn 中文') for i in range(n)]),
    kernels=[
        remove_accent_chars_regex,
        remove_accent_chars_join,
        text_unidecode.unidecode,
    ],
    labels=['regex', 'join', 'unidecode'],
    n_range=[2 ** k for k in range(22)],
    equality_check=None, relative_to=0, xlabel='str len'
)

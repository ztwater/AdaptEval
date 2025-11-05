import re

def slugify(str_: str):
    slug = re.sub(r'[^A-z0-9-]', '_', str_)
    return slug

import pytest

@pytest.mark.parametrize(
    "inp, outp_exp",
    [
        pytest.param("a b c", "a_b_c", id="whitespace -> underscore"),
        pytest.param("https://www.algorithmus-schmiede.de/kontakt/",
                     "https___www_algorithmus-schmiede_de_kontakt_", id="url"),
        pytest.param("a-b c", "a-b_c", id="minus conserved"),
    ]
)
def test_slugify(inp, outp_exp):
    assert slugify(inp) == outp_exp

#         DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                 Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#         DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
# TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
# 0. You just DO WHAT THE FUCK YOU WANT TO.
#
# Copyright © 2023 Anthony anthony@example.com
#
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the LICENSE file for more details.

import operator as op

from urllib.parse import (
    ParseResult,
    urlparse,
)

import attrs
import pytest

from phantom import Phantom
from phantom.fn import compose2


def is_url_address(value: str) -> bool:
    return any(urlparse(value))


class URL(str, Phantom, predicate=is_url_address):
    pass


# presume that an empty URL is a nonsense
def test_empty_url():
    with pytest.raises(TypeError, match="Could not parse .* from ''"):
        URL.parse("")


# is it enough now?
def test_url():
    assert URL.parse("http://")


scheme_and_netloc = op.attrgetter("scheme", "netloc")


def has_scheme_and_netloc(value: ParseResult) -> bool:
    return all(scheme_and_netloc(value))


# need a bit of FP magic 🧙 here
class ReachableURL(URL, predicate=compose2(has_scheme_and_netloc, urlparse)):
    pass


def test_empty_reachable_url():
    with pytest.raises(TypeError, match="Could not parse .* from ''"):
        ReachableURL.parse("")


# but "empty" for an URL is not just "empty string"
def test_reachable_url_probably_wrong_host():
    assert ReachableURL.parse("http://example")


def test_reachable_url():
    assert ReachableURL.parse("http://example.com")


def test_reachable_url_without_scheme():
    with pytest.raises(TypeError, match="Could not parse .* from 'example.com'"):
        ReachableURL.parse("example.com")


# constructor works too
def test_constructor():
    assert ReachableURL("http://example.com")


# but it *is* `str`
def test_url_is_str():
    assert isinstance(ReachableURL("http://example.com"), str)


# now we can write plain old classes utilizing our `URL` and `ReachableURL`

# I'm lazy...


@attrs.define
class Person:
    homepage: ReachableURL


def test_person():
    person = Person(homepage=ReachableURL("https://example.com/index.html"))

    assert person.homepage


def greet(person: Person) -> None:
    print(f"Hello! I will definitely visit you at {person.homepage}.")


if __name__ == "__main__":
    greet(Person(homepage=ReachableURL.parse("tg://resolve?username")))

# conftest.py
import pytest


class shared:
    @staticmethod
    def assert_a_general_property_between(x, y):
        ...

pytest.shared = shared

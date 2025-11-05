import pytest


class Helpers:
    @staticmethod
    def help_me():
        return "no"


@pytest.fixture
def helpers():
    return Helpers

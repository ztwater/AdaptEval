# test_module.py
from time import sleep

import pytest


def test_func_fast():
    sleep(0.1)


@pytest.mark.slow
def test_func_slow():
    sleep(10)

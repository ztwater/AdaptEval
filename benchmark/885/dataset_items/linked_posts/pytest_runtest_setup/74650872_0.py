import os
import pytest

@pytest.mark.skipif(
    not os.environ.get("MY_SPECIAL_FLAG"),
    reason="MY_SPECIAL_FLAG not set in environment"
)
def test_skip_if_no_cli_tag():
    assert True

def test_always_run():
    assert True

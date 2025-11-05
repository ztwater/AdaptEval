import pytest

pytest_plugins = ['helpers_namespace']

@pytest.helpers.register
def my_custom_assert_helper(blah):
    assert blah

# One can even specify a custom name for the helper
@pytest.helpers.register(name='assertme')
def my_custom_assert_helper_2(blah):
    assert blah

# And even namespace helpers
@pytest.helpers.asserts.register(name='me')
def my_custom_assert_helper_3(blah):
    assert blah

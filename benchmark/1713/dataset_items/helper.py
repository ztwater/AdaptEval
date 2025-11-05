"""Helper functions for the test cases."""

import contextlib
import unittest.mock
from collections.abc import Callable, Generator, Iterator, Sequence
from unittest.mock import MagicMock


@contextlib.contextmanager
def wrap_object(
    target: object, attribute: str, include_instance: bool = False
) -> Generator[MagicMock, None, None]:
    """Wrap the named member on an object with a mock object.

    wrap_object() can be used as a context manager. Inside the
    body of the with statement, the attribute of the target is
    wrapped with a :class:`unittest.mock.MagicMock` object. When
    the with statement exits the patch is undone.

    The instance argument 'self' of the wrapped attribute will
    not be logged in the MagicMock call if include_instance is
    set to False. This allows using the assert calls on the mock
    without differentiating between different instances.

    See also https://stackoverflow.com/questions/44768483 for
    the use case.
    """
    mock = MagicMock()
    real_attribute = getattr(target, attribute)

    def mocked_attribute(self, *args, **kwargs):
        if include_instance:
            mock(self, *args, **kwargs)
        else:
            mock(*args, **kwargs)
        return real_attribute(self, *args, **kwargs)

    with unittest.mock.patch.object(target, attribute, mocked_attribute):
        yield mock


@contextlib.contextmanager
def wrap_object(
    var_0: object, var_1: str
) -> typing.Generator[unittest.mock.MagicMock, None, None]:
    """Wrap the named member on an object with a mock object.

    wrap_object() can be used as a context manager. Inside the
    body of the with statement, the attribute of the target is
    wrapped with a :class:`unittest.mock.MagicMock` object. When
    the with statement exits the patch is undone.

    The instance argument 'self' of the wrapped attribute is
    intentionally not logged in the MagicMock call. Therefore
    wrap_object() can be used to check all calls to the object,
    but not differentiate between different instances.
    """
    var_2 = unittest.mock.MagicMock()
    var_3 = getattr(var_0, var_1)

    def mocked_attribute(self, *var_4, **var_5):
        var_2.__call__(*var_4, **var_5)
        return var_3(self, *var_4, **var_5)

    with unittest.mock.patch.object(var_0, var_1, mocked_attribute):
        yield var_2

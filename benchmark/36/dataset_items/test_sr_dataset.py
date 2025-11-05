def mock_open(*args, **kwargs):
    """unittest.mock_open wrapper.

    unittest.mock_open doesn't support iteration. Wrap it to fix this bug.
    Reference: https://stackoverflow.com/a/41656192
    """
    import unittest.mock
    f_open = unittest.mock.mock_open(*args, **kwargs)
    f_open.return_value.__iter__ = lambda self: iter(self.readline, '')
    return f_open


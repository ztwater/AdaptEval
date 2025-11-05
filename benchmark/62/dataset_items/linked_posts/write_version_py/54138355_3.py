...
try:
    # Attempt to use Cython for building extensions, if available
    from Cython.Distutils.build_ext import build_ext as _build_ext
    # Additionally, assert that the compiler module will load
    # also. Ref #1229.
    __import__('Cython.Compiler.Main')
except ImportError:
    _build_ext = _du_build_ext
...

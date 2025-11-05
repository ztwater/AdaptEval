class get_numpy_include(object):

    def __str__(self):
        import numpy
        return numpy.get_include()
...
my_c_lib_ext = setuptools.Extension(
    ...
    include_dirs=[get_numpy_include()]
)

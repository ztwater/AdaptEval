class MyExt(setuptools.Extension):
    def __init__(self, *args, **kwargs):
        self.__include_dirs = []
        super().__init__(*args, **kwargs)

    @property
    def include_dirs(self):
        import numpy
        return self.__include_dirs + [numpy.get_include()]

    @include_dirs.setter
    def include_dirs(self, dirs):
        self.__include_dirs = dirs


my_c_lib_ext = MyExt(
    name="my_c_lib",
    sources=["my_c_lib/some_file.pyx"]
)

setup(
    ...,
    setup_requires=['cython', 'numpy'],
)

import setuptools
from distutils.command.build import build as build_orig


class build(build_orig):

    def finalize_options(self):
        super().finalize_options()
        # I stole this line from ead's answer:
        __builtins__.__NUMPY_SETUP__ = False
        import numpy
        # or just modify my_c_lib_ext directly here, ext_modules should contain a reference anyway
        extension = next(m for m in self.distribution.ext_modules if m == my_c_lib_ext)
        extension.include_dirs.append(numpy.get_include())


my_c_lib_ext = setuptools.Extension(
    name="my_c_lib",
    sources=["my_c_lib/some_file.pyx"]
)

setuptools.setup(
    ...,
    ext_modules=[my_c_lib_ext],
    cmdclass={'build': build},
    ...
)

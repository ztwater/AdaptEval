....
# factory function
def my_build_ext(pars):
     # import delayed:
     from setuptools.command.build_ext import build_ext as _build_ext#
 
     # include_dirs adjusted: 
     class build_ext(_build_ext):
         def finalize_options(self):
             _build_ext.finalize_options(self)
             # Prevent numpy from thinking it is still in its setup process:
             __builtins__.__NUMPY_SETUP__ = False
             import numpy
             self.include_dirs.append(numpy.get_include())
     
    #object returned:
    return build_ext(pars)
...
setuptools.setup(
    ...
    cmdclass={'build_ext' : my_build_ext},
    ...
)

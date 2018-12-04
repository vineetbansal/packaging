from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

my_extension = Extension(
    name="MyExtension",
    sources=["mypyx.pyx"],
    libraries=["mylibrary"],
    library_dirs=["lib"],
    include_dirs=["include"]
)
setup(
    name="mysetupname",
    ext_modules=cythonize([my_extension])
)

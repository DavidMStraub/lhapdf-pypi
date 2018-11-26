#! /usr/bin/env python

import os
from distutils.core import setup
from distutils.extension import Extension

incdir_src = os.path.abspath("LHAPDF-6.2.1/include")
incdir_build = os.path.abspath("LHAPDF-6.2.1/include")
libdir = os.path.abspath("LHAPDF-6.2.1/src/.libs")

## Configure the C++ extension and LHAPDF package
ext = Extension("lhapdf",
                ["LHAPDF-6.2.1/wrappers/python/lhapdf.cpp"],
                include_dirs=[incdir_src, incdir_build],
                extra_compile_args=["-I/home/travis/build/include"],
                library_dirs=['/home/travis/build/lib', libdir],
                language="C++",
                libraries=["stdc++", "LHAPDF"],
                )

setup(name = "LHAPDF",
      version = "6.2.1-10",
      ext_modules = [ext],
      scripts=['bin/lhapdf'],
)

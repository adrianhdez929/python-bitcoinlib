#!/usr/bin/env python

from setuptools import setup, find_packages
import os

from crown import __version__

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = []

setup(name='python-crownlib',
      version=__version__,
      description='A python SDK for the CrownPlatform cryptocurrency',
      long_description=README,
      long_description_content_type='text/markdown',
      classifiers=[
          "Programming Language :: Python",
          "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
      ],
      url='https://github.com/adrianhdez929/python-crownlib',
      keywords='crown',
      packages=find_packages(),
      zip_safe=False,
      install_requires=requires,
      test_suite="crown.tests"
     )

##############################################################################
#
# Copyright (c) 2014 Ludia Inc and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE
#
##############################################################################

import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.txt')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except:
    README = ''
    CHANGES = ''

requires = ['pyramid >= 1.4']

docs_extras = [
    'Sphinx',
    'docutils',
    ]

testing_extras = [
    'nose',
    'mock',
    'coverage',
    'nosexcover',
    'yanc',
    ]

setup(name='pyramid_useragent',
      version='0.2',
      description='HTTP User-Agent parser for Pyramid',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Framework :: Pyramid",
        ],
      keywords='web wsgi pylons pyramid user-agent',
      author="Pior Bastida, Ludia Inc",
      author_email="pior@pbastida.net",
      url="https://bitbucket.org/pior/pyramid_useragent",
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      tests_require = ['mock'],
      install_requires = requires,
      extras_require = {
          'testing':testing_extras,
          'docs':docs_extras,
          },
      test_suite="pyramid_useragent",
      )

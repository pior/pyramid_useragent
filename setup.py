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

requires = [
    'pyramid >= 1.4',
    'user-agents',
]

docs_extras = [
    'Sphinx',
    'docutils',
    ]

dev_extras = [
    'nose',
    'mock',
    'coverage',
    'nosexcover',
    'twine',
    'six',
    ]

VERSION = '0.4.0'  # maintained by release tool

setup(name='pyramid_useragent',
      version=VERSION,
      description='HTTP User-Agent parser for Pyramid',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Framework :: Pyramid",
        ],
      keywords='web wsgi pylons pyramid user-agent',
      author="Pior Bastida",
      author_email="pior@pbastida.net",
      url="https://github.com/pior/pyramid_useragent",
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      tests_require = ['mock', 'six'],
      install_requires = requires,
      extras_require = {
          'dev':dev_extras,
          'docs':docs_extras,
          },
      test_suite="pyramid_useragent",
      )

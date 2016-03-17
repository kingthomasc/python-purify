from distutils.core import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'LONG_DESCRIPTION.rst')) as fid:
  long_desc = fid.read()

setup(
  name='python_purify',
  packages=['python_purify'],
  version='1.1.0',
  description='A python API for Web Purify',
  long_description=long_desc,
  author='Tom King, Kory Donati',
  author_email=['tomk@bixly.com', 'koryd@bixly.com'],
  url='https://github.com/kingthomasc/python-purify',
  download_url='https://github.com/kingthomasc/python-purify/tarball/1.1.0',
  keywords=['profanity', 'filter', 'web purify', 'webpurify'],
  classifiers=[],
)

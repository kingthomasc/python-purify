from distutils.core import setup

with open('LONG_DESCRIPTION.rst') as fid:
  long = fid.read()

setup(
  name='python_purify',
  packages=['python_purify'],
  version='1.0.1',
  description='A python API for Web Purify',
  long_description=long,
  author='Tom King, Kory Donati',
  author_email=['tomk@bixly.com', 'koryd@bixly.com'],
  url='https://github.com/kingthomasc/python-purify',
  download_url='https://github.com/kingthomasc/python-purify/tarball/1.0.1',
  keywords=['profanity', 'filter', 'web purify', 'webpurify'],
  classifiers=[],
)

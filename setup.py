from os import path
from setuptools import setup
here = path.abspath(path.dirname(__file__))

version_num = "2.0.0"

with open(path.join(here, 'README.rst')) as fid:
    long_desc = fid.read()

setup(
    name='python_purify',
    packages=['python_purify'],
    version=version_num,
    description='A python API for Web Purify',
    long_description=long_desc,
    author='Tom King, Kory Donati',
    author_email='tomk@bixly.com, korydonati@gmail.com',
    url='https://github.com/kingthomasc/python-purify',
    download_url='https://github.com/kingthomasc/python-purify/tarball/{ver}'.format(
        ver=version_num),
    keywords=['profanity', 'filter', 'web purify', 'webpurify'],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={
        'test': ['mock', 'pytest', 'HTTPretty'],
    },
)

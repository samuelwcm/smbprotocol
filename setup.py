#!/usr/bin/env python
# coding: utf-8

from setuptools import setup
from smbprotocol import __version__

# PyPi supports only reStructuredText, so pandoc should be installed
# before uploading package
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except ImportError:
    long_description = ''


setup(
    name='smbprotocol',
    version=__version__,
    packages=['smbprotocol'],
    install_requires=[
        'cryptography>=2.0',
        'ntlm-auth',
        'pyasn1',
        'six',
    ],
    extras_require={
        ':python_version<"2.7"': [
            'ordereddict'
        ],
    },
    author='Jordan Borean',
    author_email='jborean93@gmail.com',
    url='https://github.com/jborean93/smbprotocol',
    description='Interact with a server using the SMB 2/3 Protocol',
    long_description=long_description,
    keywords='smb smb2 smb3 cifs python',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

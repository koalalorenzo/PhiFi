#!/usr/bin/python
# -*- coding=utf-8 -*-

from distutils.core import setup
import phifi

setup(
        name='phifi',
        version=phifi.__version__,
        description=phifi.__description__,
        author=phifi.__author__,
        license=phifi.__license__,
        author_email='koalalorenzo@gmail.com',
        url='http://phifi.setale.me/',
        packages=['phifi']
    )

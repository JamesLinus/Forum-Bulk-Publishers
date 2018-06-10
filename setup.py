#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

'''

'''

setup(
    name="Application",
    version="1.0",
    author="JamesLinus",
    author_email="chocolate961025@gmail.com",
    description=(" "),
    license="GPLv3",
    keywords="Application",
    url=" ",   # 路径
    packages=['Application'],

    install_requires=[
        'python>=2.7.14',
    ],


    entry_points={'console_scripts': [
        'application = application:main',
    ]},

    
    classifiers=[
        "Development Status :: Release",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    
    zip_safe=False
)
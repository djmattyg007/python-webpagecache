#!/usr/bin/env python

from setuptools import setup, find_packages

_version = "1.0.1"
setup(
    name="webpagecache",
    version=_version,
    description="A utility class for downloading webpages and storing them in an SQLite3 database as a cache.",
    author="Matthew Gamble",
    author_email="git@matthewgamble.net",
    url="https://github.com/djmattyg007/python-webpagecache",
    download_url="https://github.com/djmattyg007/python-webpagecache/archive/{0}.zip".format(_version),
    packages=find_packages(),
    package_data={},
    data_files=[],
    license="Unlicense",
    install_requires=[]
)


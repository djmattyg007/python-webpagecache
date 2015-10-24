#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="webpagecache",
      version="1.0.0",
      description="A utility class for downloading webpages and storing them in an SQLite3 database as a cache.",
      author="Matthew Gamble",
      author_email="git@matthewgamble.net",
      url="https://github.com/djmattyg007/python-webpagecache",
      download_url="https://github.com/djmattyg007/python-webpagecache/archive/1.0.0.zip",
      packages=find_packages(),
      package_data={},
      data_files=[],
      license="Unlicense",
      install_requires=[]
      )


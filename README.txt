Webpage Cache

This is a small utility for downloading webpages and storing them in an SQLite3
database for later retrieval. It is meant to be used as a cache, to avoid
unnecessarily re-downloading the same pages over and over while building things
such as scraping tools.

This is very barebones. THe only extra functionality it has is the ability to
insert a pause before downloading a new page, as a convenience to avoid
spamming pages with many requests per second. There is nothing in the way of
invalidating cache entries at all.

This software is released into the public domain without any warranty.

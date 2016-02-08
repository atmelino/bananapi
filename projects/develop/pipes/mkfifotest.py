# !/usr/bin/python

import os, sys

# Path to be created
path = "/tmp/hourly"

os.mkfifo( path, 0644 )

print "Path is created"
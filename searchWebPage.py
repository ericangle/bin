#!/usr/bin/python

# Add better command line argument handling
# first argument is web address
# 2nd to N arguments are search terms
# prints all lines in web site that contain one of the
# search terms

import urllib
import sys

args        = (sys.argv)[1:]
site        = args[0]
searchTerms = args[1:]
output      = ''

for line in urllib.urlopen(site).read().splitlines():
  lineLower = line.lower()
  shouldPrint = False
  for searchTerm in searchTerms:
    if searchTerm in lineLower:
      shouldPrint = True
      break
  if shouldPrint:
    output = output + line

if output != '':
  print output

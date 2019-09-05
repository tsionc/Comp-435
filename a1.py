import os
import sys

filename = "sample.txt"

with open(filename, 'r') as filehandle:
    filecontent = filehandle.read()
    print (filecontent)

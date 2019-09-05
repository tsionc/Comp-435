import os
import sys


# opening and reading in file.
with open(sys.argv[1]) as f:
    filecontent = f.read()
    print (filecontent)

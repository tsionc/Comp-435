import os
import sys

from collections import Counter

# opening and reading in file.
sc= []
cc=[]
with open(sys.argv[1]) as f:
    c=Counter(c.strip() for c in f if c.strip()) #for case-insensitive search
    for  line in  c:
        if c[line]>1:
            
            cc.append(line)
            print (line, c[line] )
   

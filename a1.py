import os
import sys

from collections import Counter

# opening and reading in file.
sc= []
cc=[]
with open(sys.argv[1]) as f:
    c=Counter(int(c.rstrip(),16) for c in f if int(c.rstrip(),16)) #for case-insensitive search
    
    #print(sorted(c.keys()))
    for  line in  sorted(c.keys()):
        
        if c[line]>1:
            
            cc.append(line)
            
            print ('%x' % line, c[line] )
 

import os
import sys

from collections import Counter

# opening and reading in file.
sc= []
cc=[]
with open(sys.argv[1]) as f:
    c=Counter(int(c.strip(),16) for c in f if int(c.strip(),16)) #for case-insensitive search
    sorted (c.items())
    #print(c)
    for  line in  c:
        
        if c[line]>1:
            
            cc.append(line)
            
            print (format(line, 'x'), c[line] )
 

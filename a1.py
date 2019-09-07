import os
import sys

from collections import Counter

# opening and reading in file.
sc= []
lineduplicat=[]

    #print(f.read())
filecontent=Counter(int(filecontent,16) for filecontent in open(sys.argv[1])) #for case-insensitive search
    
    #print(sorted(c.keys()))
for  line in  sorted(filecontent.keys()):
        if filecontent[line]>1:
            lineduplicat.append('%x' % line + " " + str(filecontent[line]))
            
for i in lineduplicat:
     print(i)


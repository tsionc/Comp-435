import os
import sys
from collections import Counter

# opening and reading in the hex file as an integer and counting the lines that repeat.
filecontent=Counter(int(filecontent,16) for filecontent in open(sys.argv[1])) 
lineduplicat=[]

# first  it sorting the file in ascending order and its going to  go through the file and put the lines that are repeated 
# and the number of times they have repated into a list
for  line in  sorted(filecontent.keys()):
        if filecontent[line]>1:
            lineduplicat.append('%x' % line + " " + str(filecontent[line]))
# go through the list and print out the output of lines one by one           
for output in lineduplicat:
     print(output)


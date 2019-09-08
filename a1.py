import os
import sys
from collections import Counter

# opening and reading in the hex file as an integer and counting the lines that repeat.

filecontent=Counter(int(filecontent,16) for filecontent in open(sys.argv[1])) 
lineduplicat=[]

# first  it sorting the file in ascending order and its going to  go through the file and put the lines that are repeated 
# and the number of times they have repated into a list
#then it  prints out the outputs from the array in a newline one by one
for  line in  sorted(filecontent.keys()):
        if filecontent[line]>1:
            lineduplicat.append('%x' % line + " " + str(filecontent[line]))
print ("\n".join(lineduplicat))
         


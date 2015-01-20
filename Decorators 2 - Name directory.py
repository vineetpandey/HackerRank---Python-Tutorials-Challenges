# Enter your code here. Read input from STDIN. Print output to STDOUT
# Author : Vineet

from operator import itemgetter
from itertools import groupby

N = int(raw_input())
lst = list()
for i in range(N):
    a = raw_input()
    lst.append(a.split())
    
lst.sort(key=itemgetter(2))

for elt, items in groupby(lst, itemgetter(2)):
    for i in items:
        if i[3] == 'M':
            print "Mr.",i[0],i[1]
        else:
            print "Ms.",i[0],i[1]
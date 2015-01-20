# Enter your code here. Read input from STDIN. Print output to STDOUT
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Vineet
#
# Created:     05/12/2014
# Copyright:   (c) Vineet 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

M = raw_input()
a = raw_input()
lst1 = a.split()
newlst1 = list(map(int, lst1))
set1 = set(newlst1)
N = raw_input()
b = raw_input()
lst2 = b.split()
newlst2 = list(map(int, lst2))
set2 = set(newlst2)
x = set1.difference(set2)
#print x
y = set2.difference(set1)
#print y
z = set()
z = x.union(y)
#print z
lst = list(z)
lst = sorted(lst)
for i in range(len(lst)):
    print lst[i]
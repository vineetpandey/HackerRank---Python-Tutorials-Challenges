# Enter your code here. Read input from STDIN. Print output to STDOUT
# Author : Vineet
N = int(raw_input())
dc = dict()
lst1 = list()
for i in range(N):
    a = raw_input()
    lst1 = a.split()
    d = lst1[0]
    lst1.remove(lst1[0])
    newlst1 = list(map(float, lst1))
    dc[d] = newlst1
name = raw_input()
total = 0
if name in dc:
    marks = dc[name]
    no = len(marks)
    for num in marks:
        total += num
avg = total / no
print "%.2f" % avg
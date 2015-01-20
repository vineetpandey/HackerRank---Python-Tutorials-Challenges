# Enter your code here. Read input from STDIN. Print output to STDOUT
# Author : Vineet
s1 = str(raw_input())
s2 = str(raw_input())

# print s1.count(s2) -- for non-overlapping sequences
# Below is code for overlapping sequences
cnt = 0
for i in range(len(s1)):
    if s1[i:].startswith(s2):
		cnt += 1
    #i += x
print cnt
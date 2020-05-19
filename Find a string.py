s1 = str(input())
s2 = str(input())


t = 0
for i in range(len(s1)):
    if s1[i:].startswith(s2):
        t=t+1
		

print(t)

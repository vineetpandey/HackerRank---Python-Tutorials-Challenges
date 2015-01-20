# Enter your code here. Read input from STDIN. Print output to STDOUT
# Author : Vineet

import re

pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

N = int(raw_input())
email = [ raw_input() for i in range(N) ]
valid_email = list()
for i in email:
    if re.match(pattern,i):
        valid_email.append(i)

print sorted(valid_email)
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Author : Vineet

number = list()
N = int(raw_input())
for i in range(N):
    number.append(str(raw_input()))

def mobile(function):
    def input(number):
            return sorted([function(i) for i in number])
    return input

@mobile
def standardize(number):
	return "+91" + " " + number[-10:-5] + " " + number[-5:]

print '\n'.join(standardize(number))
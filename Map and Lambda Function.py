# Enter your code here. Read input from STDIN. Print output to STDOUT
# Author : Vineet
from itertools import islice 	# For making an iterator that returns selected elements from the iterable.
n = abs(int(raw_input()))

def fib(a=0, b=1):
    yield a
    while True:
        yield b
        a, b = b, a + b

lst = list(islice(fib(), n))
cube = lambda x: x * x * x
print list(map(cube, lst))

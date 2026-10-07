#!/usr/bin/python3
import sys

def factorial(n):
 """
    This Python script calculates the factorial of the number supplied as a command-line argument.

How it works
f = factorial(int(sys.argv[1]))
sys.argv[1] gets the first command-line argument.
int(...) converts it from a string to an integer.
factorial(...) recursively calculates n!.
print(f) displays the result.
For example:

./script.py 5
outputs:

120
because 5! = 5 × 4 × 3 × 2 × 1 = 120.

One issue
The function only explicitly handles n == 0. For negative numbers, it keeps recursing indefinitely until Python raises a RecursionError.
"""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)

#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
        Recursively calculates the factorial of a given non-negative integer.

    Parameters:
        n (int): The number for which the factorial will be calculated.

    Returns:
        int: The factorial of the given number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Convert the first command line argument to an integer,
# compute its factorial using the factorial function,
# and print the result.
f = factorial(int(sys.argv[1]))
print(f)

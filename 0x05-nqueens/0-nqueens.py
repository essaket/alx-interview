#!/usr/bin/python3
"""0. N queens"""
import sys


# Check if the number of arguments is correct
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

# Check if the argument is a digit
if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

# Convert argument to an integer
N = int(sys.argv[1])

# Ensure N is at least 4
if N < 4:
    print("N must be at least 4")
    exit(1)

def queens(n, i=0, a=[], b=[], c=[]):
    """Recursively find all solutions for placing queens"""
    if i < n:
        for j in range(n):
            # Check if placing a queen is safe
            if j not in a and i + j not in b and i - j not in c:
                # Recur to place the next queen
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        # Yield a valid solution
        yield a

def solve(n):
    """Print all solutions to the N Queens problem"""
    for solution in queens(n):
        # Format each solution as a list of [row, column] pairs
        print([[i, solution[i]] for i in range(n)])

# Solve the N Queens problem for the given N
solve(N)

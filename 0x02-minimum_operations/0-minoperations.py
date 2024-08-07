#!/usr/bin/env python3
"""0. Minimum Operations"""


def minOperations(n: int) -> int:
    """A function do a minimum operations"""
    # If n is less than or equal to 1, return 0 as it is impossible to achieve
    if n <= 1:
        return 0
    min_oper = 0  # Initialize the count of operations
    division = 2  # Start with the smallest factor
    # Loop until n is reduced to 1
    while n > 1:
        # While n is divisible by the current factor
        while n % division == 0:
            # Add the current factor to the operations count
            min_oper += division
            # Divide n by the current factor
            n /= division
        # Move to the next potential factor
        division += 1

    return min_oper # Return the total count of operations

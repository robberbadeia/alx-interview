#!/usr/bin/python3
"""
Main file for testing
"""


def minOperations(n):
    """
    Function implementation
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2
    current = n

    # Break down n into its prime factors
    while factor * factor <= current:
        while current % factor == 0:
            operations += factor
            current //= factor
        factor += 1

    # If there's any prime factor larger than sqrt(n), it'll be in `current`
    if current > 1:
        operations += current

    return operations

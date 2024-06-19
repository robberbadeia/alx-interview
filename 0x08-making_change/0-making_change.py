#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins, total):
    """
    Function implementation
    """
    if total <= 0:
        return 0
    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for i in coin:
            while(total >= i):
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1

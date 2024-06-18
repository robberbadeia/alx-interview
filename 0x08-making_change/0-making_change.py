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
    # Create a DP array with size total + 1, initially with 'infinity'
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # If dp[total] is still 'infinity', no solution was found
    return -1 if dp[total] == float('inf') else dp[total]

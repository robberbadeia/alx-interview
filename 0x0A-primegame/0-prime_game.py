#!/usr/bin/python3
"""
    Prime Game
"""


def isWinner(x, nums):
    """
        Function
    """
    # Find the maximum number to determine
    #  the range for prime number computation
    max_n = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime
    for start in range(2, int(max_n**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, max_n + 1, start):
                sieve[multiple] = False

    # List of primes up to max_n
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    # Counting wins
    maria_wins = ben_wins = 0

    # Determine the winner for each
    # game based on the number of primes up to each n
    for n in nums:
        prime_count = sum(1 for p in primes if p <= n)

        if prime_count % 2 == 1:  # Maria wins if the count is odd
            maria_wins += 1
        else:  # Ben wins if the count is even
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

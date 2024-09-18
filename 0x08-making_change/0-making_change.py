#!/usr/bin/python3
"""0. Change comes from within"""


def makeChange(coins, total):
    """Return the fewest number of coins needed to meet the total,
       or -1 if impossible."""
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    num_coins = 0

    for coin in coins:
        if total <= 0:
            break

        # Add the number of coins for this denomination
        num_coins += total // coin
        total %= coin  # Update total with the remainder

    return num_coins if total == 0 else -1  # Return -1 if exact total not met

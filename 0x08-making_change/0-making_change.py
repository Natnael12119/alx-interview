#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize the dp array with a value greater than the possible number of coins needed
    dp = [total + 1] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make 0 amount

    # Update the dp array for each coin
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still greater than total, it means it's not possible to make that amount
    return dp[total] if dp[total] != total + 1 else -1

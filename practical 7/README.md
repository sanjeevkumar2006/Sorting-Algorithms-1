# Minimum Coin Change Problem

# Summary

This project solves the **Minimum Coin Change Problem** using the **Dynamic Programming** approach.

The program takes the following inputs from the user:

- Total amount
- Available coin denominations

It then calculates the **minimum number of coins** required to make the given amount.

The program also measures the **execution time** and displays the **time complexity** and **space complexity**.

## How It Works

The program uses an array called `dp`.

`dp[i]` represents the minimum number of coins required to make the amount `i`.

intially : `dp[0]` 
in between the `dp = [float('inf')] * (amount + 1)` which adds `+1` for the amount so that system start from the `0` for goind 
get the input amount.

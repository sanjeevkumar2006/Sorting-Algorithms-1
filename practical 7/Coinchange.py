import time

def min_coin_change(amount, coins):
    # dp[i] = minimum number of coins needed to make amount i
    dp = [float('inf')] * (amount + 1)

    # 0 coins are needed to make amount 0
    dp[0] = 0

    # Calculate minimum coins for every amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]


# Take input from user
amount = int(input("Enter the amount: "))

coins = list(map(int, input(
    "Enter coin denominations separated by spaces: "
).split()))

# Measure execution time
start_time = time.perf_counter()

result = min_coin_change(amount, coins)

end_time = time.perf_counter()

execution_time = end_time - start_time


# Display result
print("\n--- Minimum Coin Change ---")
print("Amount:", amount)

if result == float('inf'):
    print("Change cannot be made using the given coins.")
else:
    print("Minimum number of coins:", result)

print("Execution Time:", execution_time, "seconds")
print("Time Complexity: O(amount × number of coins)")
print("Space Complexity: O(amount)")
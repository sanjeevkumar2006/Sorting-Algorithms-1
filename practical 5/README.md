# 0/1 Knapsack Problem — Dynamic Programming (Python)

Solves the 0/1 Knapsack problem using bottom-up DP. Takes items and capacity as user input, prints the max value, selected items, time complexity, and actual execution time.

## Input
- Number of items
- Weight and value of each item
- Knapsack capacity

## Output
- Maximum achievable value
- Selected items
- Time complexity (analytical)
- Execution time (measured)

## Key Points
- **Approach:** Bottom-up DP with a 2D table `dp[i][w]`
- **Recurrence:** `dp[i][w] = max(value + dp[i-1][w-weight], dp[i-1][w])` if item fits, else `dp[i-1][w]`
- **Time Complexity:** O(n × W)
- **Space Complexity:** O(n × W) — reducible to O(W) without backtracking
- **Constraint:** Each item used at most once (0/1, no fractions)

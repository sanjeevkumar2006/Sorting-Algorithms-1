import time

def knapsack(weights, values, capacity, n):
    """
    Solves 0/1 Knapsack problem using Dynamic Programming.
    
    Time Complexity: O(n * capacity)
    Space Complexity: O(n * capacity)
    """
    # dp[i][w] = max value using first i items with capacity w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                # Max of (including item i-1) or (excluding item i-1)
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find which items were selected
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)  # store index of item
            w -= weights[i - 1]

    selected_items.reverse()
    return dp[n][capacity], selected_items


def main():
    print("=== 0/1 Knapsack Problem (Dynamic Programming) ===\n")

    # Taking input from user
    n = int(input("Enter number of items: "))

    weights = []
    values = []

    for i in range(n):
        w = int(input(f"Enter weight of item {i + 1}: "))
        v = int(input(f"Enter value of item {i + 1}: "))
        weights.append(w)
        values.append(v)

    capacity = int(input("Enter knapsack capacity: "))

    # Start timing
    start_time = time.perf_counter()

    max_value, selected_items = knapsack(weights, values, capacity, n)

    # End timing
    end_time = time.perf_counter()
    execution_time = end_time - start_time

    # Output results
    print("\n=== Results ===")
    print(f"Maximum value that can be obtained: {max_value}")
    print("Items included (0-indexed):", selected_items)
    print("Items included (weight, value):", [(weights[i], values[i]) for i in selected_items])

    print("\n=== Complexity Analysis ===")
    print(f"Time Complexity: O(n * capacity) = O({n} * {capacity}) = O({n * capacity})")
    print(f"Space Complexity: O(n * capacity) = O({n * capacity})")

    print("\n=== Performance ===")
    print(f"Execution Time: {execution_time:.8f} seconds")


if __name__ == "__main__":
    main()
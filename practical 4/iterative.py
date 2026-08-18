import time

def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


# Take input from user
n = int(input("Enter a number: "))

# Measure execution time
start_time = time.perf_counter()

result = factorial_iterative(n)

end_time = time.perf_counter()

execution_time = end_time - start_time

# Output
print("\n--- Iterative Method ---")
print("Number:", n)
print("Factorial:", result)
print("Execution Time:", execution_time, "seconds")
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")
import time

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# Take input from user
n = int(input("Enter a number: "))

# Measure execution time
start_time = time.perf_counter()

result = factorial_recursive(n)

end_time = time.perf_counter()

execution_time = end_time - start_time

# Output
print("\n--- Recursive Method ---")
print("Number:", n)
print("Factorial:", result)
print("Execution Time:", execution_time, "seconds")
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")
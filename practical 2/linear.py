## Linear Search in Python
import time

# Take input from user
n = int(input("Enter the number of elements: "))

numbers = []

print("Enter the elements:")
for i in range(n):
    value = int(input(f"Element {i + 1}: "))
    numbers.append(value)

# Take search element from user
target = int(input("Enter the element to search: "))

# Start measuring execution time
start_time = time.perf_counter()

# Linear Search
found = False
position = -1

for i in range(n):
    if numbers[i] == target:
        found = True
        position = i
        break

# Stop measuring execution time
end_time = time.perf_counter()

# Calculate execution time
execution_time = end_time - start_time

# Display result
print("\n--- Linear Search Result ---")

if found:
    print(f"Element {target} found at index {position}")
    print(f"Position: {position + 1}")
else:
    print(f"Element {target} not found")

# Display time complexity
print("\n--- Time Complexity ---")
print("Best Case   : O(1)")
print("Average Case: O(n)")
print("Worst Case  : O(n)")

# Display execution time
print("\n--- Execution Time ---")
print(f"Execution Time: {execution_time:.10f} seconds")


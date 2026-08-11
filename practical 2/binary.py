# Binary Search in Python
# Takes input from the user
# Displays execution time and time complexity

import time

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Take number of elements
n = int(input("Enter the number of elements: "))

# Take sorted list from the user
print("Enter the elements in sorted order:")
arr = list(map(int, input().split()))

# Check if the correct number of elements is entered
if len(arr) != n:
    print("Error: Number of elements entered does not match.")
else:
    # Take the element to search
    target = int(input("Enter the element to search: "))

    # Record start time
    start_time = time.perf_counter()

    # Perform Binary Search
    result = binary_search(arr, target)

    # Record end time
    end_time = time.perf_counter()

    # Calculate execution time
    execution_time = end_time - start_time

    # Display result
    if result != -1:
        print(f"\nElement {target} found at index {result}.")
    else:
        print(f"\nElement {target} not found in the list.")

    # Display execution time
    print(f"Execution Time: {execution_time:.10f} seconds")

    # Display time complexity
    print("\nTime Complexity:")
    print("Best Case    : O(1)")
    print("Average Case : O(log n)")
    print("Worst Case   : O(log n)")

    # Display space complexity
    print("Space Complexity: O(1)")
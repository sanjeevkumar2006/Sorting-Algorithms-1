import time


def selection_sort(arr):
    """
    Sorts a list using the Selection Sort algorithm.

    Time Complexity:
        Best Case:    O(n^2) -> still scans the remaining list every pass, even if already sorted
        Average Case: O(n^2)
        Worst Case:   O(n^2)

    Space Complexity: O(1) -> sorting is done in-place
    """
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Take input from the user
user_input = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

# Measure execution time
start_time = time.perf_counter()
sorted_numbers = selection_sort(numbers)
end_time = time.perf_counter()

execution_time = end_time - start_time

# Display results
print("Sorted list:", sorted_numbers)
print(f"Execution time: {execution_time:.8f} seconds")
print("\nTime Complexity:")
print("  Best Case    : O(n^2)")
print("  Average Case : O(n^2)")
print("  Worst Case   : O(n^2)")
print("Space Complexity: O(1)")
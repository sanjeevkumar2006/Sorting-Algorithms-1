import time


def bubble_sort(arr):
    """
    Sorts a list using the Bubble Sort algorithm.

    Time Complexity:
        Best Case:    O(n)    -> when the list is already sorted (with the swapped flag optimization)
        Average Case: O(n^2)
        Worst Case:   O(n^2)  -> when the list is sorted in reverse order

    Space Complexity: O(1) -> sorting is done in-place
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # list is already sorted, exit early
    return arr


# Take input from the user
user_input = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

# Measure execution time
start_time = time.perf_counter()
sorted_numbers = bubble_sort(numbers)
end_time = time.perf_counter()

execution_time = end_time - start_time

# Display results
print("Sorted list:", sorted_numbers)
print(f"Execution time: {execution_time:.8f} seconds")
print("\nTime Complexity:")
print("  Best Case    : O(n)")
print("  Average Case : O(n^2)")
print("  Worst Case   : O(n^2)")
print("Space Complexity: O(1)")
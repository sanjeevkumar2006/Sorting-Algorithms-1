import time


def merge_sort(arr):
    """
    Sorts a list using the Merge Sort algorithm (divide and conquer).

    Time Complexity:
        Best Case:    O(n log n)
        Average Case: O(n log n)
        Worst Case:   O(n log n) -> always splits and merges consistently, regardless of input order

    Space Complexity: O(n) -> requires extra space for temporary sub-arrays during merging
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        merge(arr, left_half, right_half)

    return arr


def merge(arr, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


# Take input from the user
user_input = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

# Measure execution time
start_time = time.perf_counter()
sorted_numbers = merge_sort(numbers)
end_time = time.perf_counter()

execution_time = end_time - start_time

# Display results
print("Sorted list:", sorted_numbers)
print(f"Execution time: {execution_time:.8f} seconds")
print("\nTime Complexity:")
print("  Best Case    : O(n log n)")
print("  Average Case : O(n log n)")
print("  Worst Case   : O(n log n)")
print("Space Complexity: O(n)")
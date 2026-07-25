import time


def quick_sort(arr, low, high):
    """
    Sorts a list using the Quick Sort algorithm (in-place, Lomuto partition scheme).

    Time Complexity:
        Best Case:    O(n log n) -> balanced partitions each time
        Average Case: O(n log n)
        Worst Case:   O(n^2)     -> already sorted or reverse-sorted input with a poor pivot choice

    Space Complexity: O(log n) -> due to recursion stack (in-place sorting)
    """
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr


def partition(arr, low, high):
    pivot = arr[high]  # choosing the last element as pivot
    i = low - 1        # index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Take input from the user
user_input = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

# Measure execution time
start_time = time.perf_counter()
sorted_numbers = quick_sort(numbers, 0, len(numbers) - 1)
end_time = time.perf_counter()

execution_time = end_time - start_time

# Display results
print("Sorted list:", sorted_numbers)
print(f"Execution time: {execution_time:.8f} seconds")
print("\nTime Complexity:")
print("  Best Case    : O(n log n)")
print("  Average Case : O(n log n)")
print("  Worst Case   : O(n^2)")
print("Space Complexity: O(log n)")
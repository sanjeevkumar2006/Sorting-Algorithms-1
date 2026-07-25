import time


def insertion_sort(arr):
    """
    Sorts a list using the Insertion Sort algorithm.

    Time Complexity:
        Best Case:    O(n)   -> when the list is already sorted, only one comparison per element is needed
        Average Case: O(n^2)
        Worst Case:   O(n^2) -> when the list is sorted in reverse order

    Space Complexity: O(1) -> sorting is done in-place
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Shift elements of the sorted portion that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Take input from the user
user_input = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

# Measure execution time
start_time = time.perf_counter()
sorted_numbers = insertion_sort(numbers)
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
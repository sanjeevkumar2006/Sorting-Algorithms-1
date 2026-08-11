import time

# Function to maintain the Max Heap property
def heapify(arr, n, i):
    largest = i          # Assume root is largest
    left = 2 * i + 1     # Left child
    right = 2 * i + 2    # Right child

    # Check if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


# Max Heap Sort function
def max_heap_sort(arr):
    n = len(arr)

    # Step 1: Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):

        # Move maximum element to the end
        arr[0], arr[i] = arr[i], arr[0]

        # Heapify the reduced heap
        heapify(arr, i, 0)


# -------------------------------
# Main Program
# -------------------------------

# Take input from user
user_input = input("Enter numbers separated by spaces: ")

# Convert input into integer list
arr = list(map(int, user_input.split()))

print("\nOriginal Array:", arr)

# Measure execution time
start_time = time.perf_counter()

# Perform Max Heap Sort
max_heap_sort(arr)

end_time = time.perf_counter()

# Calculate execution time
execution_time = end_time - start_time

# Display results
print("Sorted Array:", arr)

print("\nTime Complexity:")
print("Best Case    : O(n log n)")
print("Average Case : O(n log n)")
print("Worst Case   : O(n log n)")

print("\nSpace Complexity: O(log n)")

print(f"Execution Time: {execution_time:.10f} seconds")
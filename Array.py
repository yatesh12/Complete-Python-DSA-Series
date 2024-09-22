# ******************* Concepts Covered *******************
# -Initializing Arrays: Demonstrating 1D, 2D, and 3D arrays.
# -Traversal: Iterating over arrays.
# -Insertion & Deletion: Basic insert and delete operations in arrays.
# -Searching: Linear search and binary search algorithms.
# -Sorting: Bubble sort, selection sort, quicksort, and merge sort.
# -Reversing: Reversing the array.
# -Array Slicing: Extracting sub-arrays.
# -Rotation: Left rotation of an array.
# -Merging: Merging two arrays.
# -Matrix Operations: Addition, multiplication, and transpose using numpy.
# -Flattening & Reshaping: Converting multi-dimensional arrays into 1D and reshaping them.
# -Multi-dimensional Arrays: Demonstrating 3D arrays with numpy.

import numpy as np

# 1. Initializing Arrays
one_d_array = [10, 20, 30, 40, 50]
two_d_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("1D Array:", one_d_array)
print("2D Array (Matrix):")
for row in two_d_array:
    print(row)

# 2. Traversal
print("\nArray Traversal:")
for i in one_d_array:
    print(i, end=" ")
print("\n")

# 3. Insertion
one_d_array.insert(3, 35)  # Insert 35 at index 3
print("After Insertion:", one_d_array)

# 4. Deletion
del one_d_array[2]  # Delete element at index 2
print("After Deletion:", one_d_array)

# 5. Searching
search_element = 40
if search_element in one_d_array:
    print(f"{search_element} found at index {one_d_array.index(search_element)}")
else:
    print(f"{search_element} not found.")

# 6. Sorting

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

unsorted_array = [64, 25, 12, 22, 11]
print("\nSorting Algorithms:")
print("Bubble Sorted Array:", bubble_sort(unsorted_array.copy()))
print("Selection Sorted Array:", selection_sort(unsorted_array.copy()))
print("Quick Sorted Array:", quick_sort(unsorted_array.copy()))
print("Merge Sorted Array:", merge_sort(unsorted_array.copy()), unsorted_array)

# 7. Searching Algorithms

# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary Search (Array must be sorted)
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

sorted_array = sorted(one_d_array)
print("\nSearching Algorithms:")
print("Linear Search Result for 35:", linear_search(one_d_array, 35))
print("Binary Search Result for 40:", binary_search(sorted_array, 40))

# 8. Array Reversal
one_d_array.reverse()
print("\nReversed Array:", one_d_array)

# 9. Array Slicing
print("Array Slice (from index 1 to 4):", one_d_array[1:5])

# 10. Array Rotation (Left Rotation by 2)
def rotate_left(arr, d):
    return arr[d:] + arr[:d]

rotated_array = rotate_left(one_d_array, 2)
print("Left Rotated Array (by 2):", rotated_array)

# 11. Merging Arrays
array_1 = [1, 3, 5]
array_2 = [2, 4, 6]
merged_array = array_1 + array_2
print("\nMerged Array:", merged_array)

# 12. Matrix Operations using NumPy
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Matrix Addition
matrix_sum = np.add(matrix_a, matrix_b)
print("\nMatrix Addition:\n", matrix_sum)

# Matrix Multiplication
matrix_product = np.dot(matrix_a, matrix_b)
print("Matrix Multiplication:\n", matrix_product)

# Matrix Transposition
matrix_transpose = np.transpose(matrix_a)
print("Matrix Transpose:\n", matrix_transpose)

# 13. Array Flattening (Converting 2D to 1D)
flattened_array = np.ravel(two_d_array)
print("\nFlattened 2D Array:", flattened_array)

# 14. Reshaping Arrays
reshaped_array = np.reshape(flattened_array, (3, 3))
print("Reshaped Array (3x3):\n", reshaped_array)

# 15. Multi-dimensional Arrays (3D)
three_d_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print("\n3D Array:")
print(three_d_array)

# 16. Creation of array using array method:
import array as arr
number = arr.array("i",[20,30,40])
print("array elements are: ",number)
for i in number:
    print(i)
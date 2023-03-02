import sys

# This is the partition function. It takes the array, the lower bound, and the upper bound, and returns where to split the list.
def partition(a, l, h):
    # Pivot value
    pivot = a[l]
    # Indices: i starts from the lower bound and j starts from the upper
    i = l
    j = h - 1
    # While the indices don't overlap:
    while i < j:
        # Find a value greater than the pivot that should be less
        while a[i] <= pivot:
            i += 1
        # Find a value less than the pivot that should 
        while a[j] > pivot:
            j -= 1
        # If the values didn't overlap
        if i < j:
            # swap the values at the indices
            a[i], a[j] = a[j], a[i]
    # swap the pivot with the smaller value
    a[l], a[j] = a[j], a[l]
    return j

def quicksort(a, l, h):
    # If there is more than one element
    if (l < h):
        # Divide the list
        j = partition(a, l, h)
        # Perform quicksort on both sides
        quicksort(a, l, j)
        quicksort(a, j + 1, h)

array = [10, 29, 3, 49, 33, 12, 59, 100, 4]
# Necessary when the pivot is the first value
array.append(sys.maxsize)
quicksort(array, 0, len(array) - 1)
array.pop(len(array) - 1)
print(array)
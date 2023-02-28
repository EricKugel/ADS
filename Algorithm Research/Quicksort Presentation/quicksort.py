import sys

def partition(a, l, h):
    pivot = a[l]
    i = l
    j = h - 1
    while i < j:
        while a[i] <= pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def quicksort(a, l, h):
    if (l < h):
        j = partition(a, l, h)
        quicksort(a, l, j)
        quicksort(a, j + 1, h)

array = [10, 29, 3, 49, 33, 12, 59, 100, 4]
array.append(sys.maxsize)
quicksort(array, 0, len(array) - 1)
array.pop(len(array) - 1)
print(array)
# A quicksort algorithm, using wikipedia's psuedocode

def quicksort(array, low, high):
    if low >= high or low < 0:
        return
    p = partition(array, low, high)

    quicksort(array, low, p - 1)
    quicksort(array, p + 1, high)

def partition(array, low, high):
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    i += 1
    array[i], array[high] = array[high], array[i]
    return i

array = [6,2,8,4,7,52,87,1,654,314,76,32,67,23,76,89,65,3,132,4,65,8,32,65,2,1,1,76,8,3,5,67,7,87,9,90,67,65,54,34,2,2]
quicksort(array, 0, len(array) - 1)

print(array)

def normal_sort(array):
    i = 0
    for j_index, j in enumerate(array):
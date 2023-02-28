# HOW IT WORKS

## what is a sorted element?
 - The correct spot for the smallest element is at the beginning of the list.
 - The correct spot for any element is the spot where every element to the left is smaller, and every element to the right is bigger.

## divide and conquer
 - start with the whole list, and find where to split it.
 - take the first element (the pivot value) and find where its spot is
 - perform quicksort on both sides

## partitioning
 - start at the low and high values
 - swap each if they are bigger and smaller than the partition
 - stop when the indices are overlapping
 - swap the pivot with the thing
 - return the partition point

## example (python)
 - noice

# ANALYSIS
 - time analysis
 - best case
 - worst case
 - ways to improve

# USAGE
 - invented
 - where it's used

# SOURCES
 - https://www.youtube.com/watch?v=7h1s2SojIRw
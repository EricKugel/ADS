# Find the min of a list of numbers in O(n^2) time
def o_n_2(numbers):
    for num_a in numbers:
        for num_b in numbers:
            if num_b < num_a:
                break
        else:
            return num_a

# Find the min in O(n) time
def o_n(numbers):
    min_num = 1000000000
    for number in numbers:
        if number < min_num:
            min_num = number
    return min_num

print(o_n_2({12,435,5,56,87,2,568,5,3,342,3687,2,6,}))
print(o_n({12,435,5,56,87,2,568,5,3,342,3687,2,6,}))
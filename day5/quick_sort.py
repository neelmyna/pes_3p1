import partition

def quickSort_array(numbers, low, high):
    if low < high:
        pivot_index = partition.partition(numbers, low, high)
        quickSort_array(numbers, low, pivot_index-1)
        quickSort_array(numbers, pivot_index+1, high)


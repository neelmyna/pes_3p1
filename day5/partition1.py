def partition(numbers):
    k = 0
    pivot = numbers[-1]
    for i in range(1, len(numbers)-1):
        if numbers[i] < pivot:
            numbers[i], numbers[k] = numbers[k], numbers[i]
            k += 1
    numbers[k], numbers[-1] = numbers[-1], numbers[k]

numbers = [34, 32, 21, 12, 11, 9, 5, 55, 43, 30]

print(f'Before Partition, Array is {numbers}')
partition(numbers)
print(f'After Partition, Array is {numbers}')

'''
x = 5
y = 10

x, y = y, x  (10, 5)

0 1 2 3 4 5 6 7

4 3 8 6 1 1 9 5
4 3 1 6 8 1 9 5
4 3 1 1 8 6 9 5
4 3 1 1 5 6 9 8

k=0 1 2 2 2 3 4
i=0 1 2 3 4 5 6
p=5

quickSort(numbers, low, high):
    if low < high:
        pivot_index = partition(numbers, low, high)
        quickSort(numbers, low, pivot_index-1)
        quickSort(numbers, pivot_index+1, high)


'''
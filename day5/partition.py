def partition(numbers, low, high):
    k = low
    pivot = numbers[high]
    for i in range(low, high):
        if numbers[i] < pivot:
            numbers[i], numbers[k] = numbers[k], numbers[i]
            k += 1
    numbers[k], numbers[high] = numbers[high], numbers[k]
    print(numbers)
    return k

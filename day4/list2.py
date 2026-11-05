numbers = [23, 19, 7, 17, 11, 13, 5, 2]
list1 = [10, 20, 30]

numbers.append(list1)
print(numbers)
print(numbers[0])
print(numbers[8])
print(numbers[8][1])


numbers = [23, 19, 7, 17, 11, 13, 5, 2]
list2 = [50, 500, 5000]

numbers.extend(list2)
print(numbers)


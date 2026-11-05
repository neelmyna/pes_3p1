numbers = []
numbers = list()
numbers = [23, 19, 7, 17, 11, 13, 5, 2] # initializing a list

'''
add new element to the list
    1. Add at end       append()
    2. Add at index     insert()
Delete an element from list
    1. delete element from end of list      pop()
    2. delete specific element              remove()
We can add multiple elements to a list using extend() which adds elements of list2 to list1.
'''

numbers = [23, 19, 7, 17, 11, 13, 5, 2] # initializing a list
temp_list = sorted(numbers)
temp_list = sorted(numbers, reverse=True)

print(f'Numbers = {numbers}')
print(f'Temp List = {temp_list}')

num = 90 # This is not iterable, because there is only one value
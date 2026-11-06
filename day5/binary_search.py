# Read the data from command line
# Read the data using inpput() and list comprehension
# Read the data from a File

import sys

def do_binary_search(numbers, search_element):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == search_element:
            return mid
        elif search_element < numbers[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

numbers = [int(element) for element in sys.argv[1:]]
numbers.sort()

print(f'The input list is {numbers}')
search_element = int(input('Enter the search element: '))

index_of_search_element = do_binary_search(numbers, search_element)

if index_of_search_element == -1:
    print(f'{search_element} not found in the list')
else:
    print(f'{search_element} found at index {index_of_search_element}')
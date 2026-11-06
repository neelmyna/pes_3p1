#from quick_sort import quickSort_array as q
from quick_sort import quickSort_array

numbers = [34, 32, 21, 12, 11, 9, 5, 55, 43, 30]

print(f'Before Sorting, Array is {numbers}')
quickSort_array(numbers, 0, len(numbers)-1)
print(f'After Sorting, Array is {numbers}')

'''
import quick_sort
quick_sort.quickSort_array()


from quick_sort import quickSort_array as qa
qa.quickSort_array()
'''
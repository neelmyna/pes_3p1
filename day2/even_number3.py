# Check if a number is Even or Odd.

input_number = int(input('Enter a number to check if it is Even: '))

if input_number % 2 == 0:
    print(input_number, 'is an Even number')
else:
    print(f'{input_number} is an Odd number')
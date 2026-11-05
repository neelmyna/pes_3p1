numbers = []
print('Enter numbers of the list (Enter -1 to stop)')
while True:
    number = float(input())
    if number == -1.0:
        break
    #numbers.append(number)
    numbers.insert(0, number)

print(f'The List is {numbers}')
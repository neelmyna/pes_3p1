import sys
import pdb

pdb.set_trace()

input_number = int(sys.argv[1])
max_digit = 0
min_digit = 9

temp = input_number
while temp != 0:
    remainder_digit = temp % 10
    
    if max_digit < remainder_digit:
        max_digit = remainder_digit
    if min_digit > remainder_digit:
        min_digit = remainder_digit

    temp = temp // 10

print(f'Max digit is {max_digit}, Min digit is {min_digit}')

'''
ip=675

i=1
    t=675
    r=5
    mx=5
    mi=5
    t=67
i=2
    t=67
    r=7
    mx=7
    mi=5
    t=6
i=3
    t=6
    r=6
    mx=7
    mi=5
    t=0
i=4 CONDITION FAILS
'''

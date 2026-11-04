import sys

def my_range(*var_args): # (5, 25)
    if len(var_args) <= 0 or len(var_args) >= 4:
        raise TypeError
    i = 0
    if len(var_args) == 1:
        while i < var_args[0]:
            yield i
            i += 1
    elif len(var_args) == 2:
        i = var_args[0]
        while i < var_args[1]:
            yield i
            i += 1 
    elif len(var_args) == 3:
        i = var_args[0]
        if var_args[2] == 0:
            raise ValueError
        elif var_args[2] > 0:
            while i < var_args[1]:
                yield i
                i += var_args[2]
        else:
            while i > var_args[1]:
                yield i
                i = i + var_args[2]

for i in my_range(int(sys.argv[2])):
    print(i, end= '  ')
print()

# my_range(m, n)
for i in my_range(int(sys.argv[1]), int(sys.argv[2])):
    print(i, end= '  ')
print()

# my_range(m, n, increment)
for i in my_range(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])):
    print(i, end= '  ')
print()

# my_range(m , n, decrement)
for i in my_range(int(sys.argv[2]), int(sys.argv[1]), int(sys.argv[4])):
    print(i, end= '  ')
print()

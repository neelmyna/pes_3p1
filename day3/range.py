import sys

# python range.py 20 50 2 -3

# range(n)
for i in range(int(sys.argv[2])):
    print(i, end= '  ')
print()

# range(m, n)
for i in range(int(sys.argv[1]), int(sys.argv[2])):
    print(i, end= '  ')
print()

# range(m, n, increment)
for i in range(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])):
    print(i, end= '  ')
print()

# range(m , n, decrement)
for i in range(int(sys.argv[2]), int(sys.argv[1]), int(sys.argv[4])):
    print(i, end= '  ')
print()

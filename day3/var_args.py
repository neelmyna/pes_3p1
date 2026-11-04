def my_function(*args):
    print(args) # print all elements of args
    print(type(args)) # print DT of args
    print(len(args))
    print(args[0], args[-1]) # print 1st and last elements of args
    

my_function(1, 2, 4, 5, 8)
my_function(100)
my_function(1, 2)
my_function(1, 2, 4, 'mandya', [8, 9])
my_function()
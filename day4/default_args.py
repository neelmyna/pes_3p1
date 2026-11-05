def find_rectangle_area(length=14, breadth=24):
    print(f'Rectangle Length={length}, Breadth={breadth}')
    area = length * breadth
    return area

length = 10
breadth = 16

area = find_rectangle_area(breadth=length, length=breadth)#Named Args
area = find_rectangle_area(breadth)#value of breadth goes to 1st Arg length
area = find_rectangle_area() # both default values will be taken
area = find_rectangle_area(25) # 25 is set to length and default value is set to breadth
area = find_rectangle_area(breadth=22, length=24)#Named Args
area = find_rectangle_area(breadth=22, length=24)#Named Args
area = find_rectangle_area(length, breadth)
area = find_rectangle_area(length)

print(f'Rectangle Area = {area} sq units')
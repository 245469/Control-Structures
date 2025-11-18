x = int(input('Enter x: '))
y = int(input('Enter y: '))

if x == 0 and y == 0:
    print(f'Point P({x},{y}) is located in the position (0,0) of the coordinate system')
elif x > 0 and y > 0:
    print(f'Point P({x},{y}) is located in the first quadrant of the coordinate system')
elif x > 0 and y < 0:
    print(f'Point P({x},{y}) is located in the second quadrant of the coordinate system')
elif x < 0 and y < 0:
    print(f'Point P({x},{y}) is located in the third quadrant of the coordinate system')
elif x < 0 and y > 0:
    print(f'Point P({x},{y}) is located in the fourth quadrant of the coordinate system')
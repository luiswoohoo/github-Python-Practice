''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

''' Type your code here. '''
found_solution = False

for x in range(-10, 11):
    for y in range(-10, 11):

        if ((a * x) + (b * y) == c) and ((d * x) + (e * y) == f):
            print('x =', x, ',', 'y =', y)

            found_solution = True
            break

    if found_solution:
        break

if not found_solution:
    print('There is no solution')

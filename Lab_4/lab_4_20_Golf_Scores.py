par = int(input())
strokes = int(input())

score = par - strokes

if (3 <= par <= 5):
    if score == 2:
        print('Eagle')
    elif score == 1:
        print('Birdie')
    elif score == 0:
        print('Par')
    elif score == -1:
        print('Bogey')
else:
    print('Error')
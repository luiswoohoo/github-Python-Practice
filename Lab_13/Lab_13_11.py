def draw_triangle(base):
    if base == 1:
        print('         *')
        return '        '
    else:
        spaces = (draw_triangle(base - 2).count(' '))
        print(' ' * spaces, '*' * base, sep='')
        return ' ' * (spaces - 1)


if __name__ == '__main__':
    base_length = int(input())
    draw_triangle(base_length)

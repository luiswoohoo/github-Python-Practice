try:
    user_num = input()
    div_num = input()

    quotient = int(user_num) // int(div_num)
    print(quotient)

except ValueError:
    print('Input Exception: invalid literal for int() with base 10: \'{}\''.format(user_num))

except ZeroDivisionError:
    print('Zero Division Exception: integer division or modulo by zero')
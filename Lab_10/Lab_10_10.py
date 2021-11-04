try:
    user_num = input()
    div_num = input()

    quotient = int(user_num) // int(div_num)
    print(quotient)

except ValueError as ve_exception:
    print('Input Exception: {}'.format(ve_exception))

except ZeroDivisionError as zd_exception:
    print('Zero Division Exception: {}'.format(zd_exception))

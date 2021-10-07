def swap_values(user_val1, user_val2):
    return user_val2, user_val1


value1 = int(input())
value2 = int(input())

swapped_values = swap_values(value1, value2)

print('{} {}'.format(swapped_values[0], swapped_values[1]))

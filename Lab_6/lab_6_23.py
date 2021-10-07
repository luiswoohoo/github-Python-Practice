def exact_change(user_total):
    num_dollars = user_total // 100
    num_quarters = (user_total % 100) // 25
    num_dimes = ((user_total % 100) % 25) // 10
    num_nickels = (((user_total % 100) % 25) % 10) // 5
    num_pennies = ((((user_total % 100) % 25) % 10) % 5) // 1

    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies

def print_exact_change(list_of_change):

    if list_of_change[0] == 1:
        print(list_of_change[0], 'Dollar')
    elif list_of_change[0] > 1:
        print(list_of_change[0], 'Dollars')

    if list_of_change[1] == 1:
        print(list_of_change[1], 'Quarter')
    elif list_of_change[1] > 1:
        print(list_of_change[1], 'Quarters')

    if list_of_change[2] == 1:
        print(list_of_change[2], 'Dime')
    elif list_of_change[2] > 1:
        print(list_of_change[2], 'Dimes')

    if list_of_change[3] == 1:
        print(list_of_change[3], 'Nickel')
    elif list_of_change[3] > 1:
        print(list_of_change[3], 'Nickels')

    if list_of_change[4] == 1:
        print(list_of_change[4], 'Penny')
    elif list_of_change[4] > 1:
        print(list_of_change[4], 'Pennies')


input_val = int(input())
num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

if input_val <= 0:
    print('no change')
else:
    total_change = exact_change(input_val)
    print_exact_change(total_change)

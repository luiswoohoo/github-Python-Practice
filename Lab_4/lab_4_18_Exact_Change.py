change = int(input())

if change <= 0:
    print('No change')

dollars = change // 100
if dollars == 1:
    print(dollars, 'Dollar')
elif dollars > 1:
    print(dollars, 'Dollars')

quarters = (change % 100) // 25
if quarters == 1:
    print(quarters, 'Quarter')
elif quarters > 1:
    print(quarters, 'Quarters')

dimes = ((change % 100) % 25) // 10
if dimes == 1:
    print(dimes, 'Dime')
elif dimes > 1:
    print(dimes, 'Dimes')

nickels = (((change % 100) % 25) % 10) // 5
if nickels == 1:
    print(nickels, 'Nickel')
elif nickels > 1:
    print(nickels, 'Nickels')

pennies = ((((change % 100) % 25) % 10) % 5) // 1
if pennies == 1:
    print(pennies, 'Penny')
elif pennies > 1:
    print(pennies, 'Pennies')

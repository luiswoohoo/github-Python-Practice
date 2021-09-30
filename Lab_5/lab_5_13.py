import random

# Dictionary to store sum of dice each time they are rolled
sum_stats = {
    2: 0, # Number of times sum of dice is 2
    3: 0, # Number of times sum of dice is 3
    4: 0, # etc.
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0
}

num_rolls = int(input('Enter number of rolls:\n'))

if num_rolls >= 1:
    for i in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_total = die1 + die2

        # Count the number of times the sum of the randomly rolled dice
        # equals each possible value from 2 to 12
        sum_stats[roll_total] += 1

        print('Roll {} is {} ({} + {})'.format(i + 1, roll_total, die1, die2))

    print('\nDice roll statistics:')
    print('2s:', sum_stats[2])
    print('3s:', sum_stats[3])
    print('4s:', sum_stats[4])
    print('5s:', sum_stats[5])
    print('6s:', sum_stats[6])
    print('7s:', sum_stats[7])
    print('8s:', sum_stats[8])
    print('9s:', sum_stats[9])
    print('10s:', sum_stats[10])
    print('11s:', sum_stats[11])
    print('12s:', sum_stats[12])

else:
    print('Invalid number of rolls. Try again.')

import random
random.seed(5)

keep_bidding = '-'
next_bid = 0

while keep_bidding != 'n':
   next_bid = next_bid + random.randint(1, 10)
   print('I\'ll bid ${}!'.format(next_bid))
   print('Continue bidding?', end=' ')
   keep_bidding = input()
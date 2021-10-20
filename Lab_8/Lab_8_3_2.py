#Lebron James: Statistics for 2003/2004 - 2012/2013
games_played = [79, 80, 79, 78, 75, 81, 76, 79, 62, 76]
points = [1654, 2175, 2478, 2132, 2250, 2304, 2258, 2111, 1683, 2036]
assists = [460, 636, 814, 701, 771, 762, 773, 663, 502, 535]
rebounds = [432, 588, 556, 526, 592, 613, 554, 590, 492, 610]

# Print total points
print('Total points:', sum(points))

# Print Average PPG
print('Average PPG: {:.2f}'.format(sum(points)/sum(games_played)))

# Print best scoring years (Ex: 2004/2005)
print('Best score:', max(points))
for pos, point in enumerate(points):
    if point == max(points):
        print('Best scoring year: 20{:0>2}/20{:0>2}'.format(pos + 3, pos + 4))

# Print worst scoring years (Ex: 2004/2005)
print('Worst score:', min(points))
for pos, point in enumerate(points):
    if point == min(points):
        print('Worst scoring year: 20{:0>2}/20{:0>2}'.format(pos + 3, pos + 4))

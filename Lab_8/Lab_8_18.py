user_input = input().split()

list_of_integers = []
for number in user_input:
    list_of_integers.append(int(number))

list_of_range = []
user_input = input().split()
for number in user_input:
    list_of_range.append(int(number))

lower_bound = list_of_range[0]
upper_bound = list_of_range[1]

for i in list_of_integers:
    if (lower_bound <= i <= upper_bound):
        print(i, end=' ')


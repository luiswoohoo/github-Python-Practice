import math

user_input = input().split()

list_of_integers = []
for number in user_input:
    list_of_integers.append(int(number))

average = math.ceil(sum(list_of_integers) / len(list_of_integers))
print('{} {}'.format(average, max(list_of_integers)))

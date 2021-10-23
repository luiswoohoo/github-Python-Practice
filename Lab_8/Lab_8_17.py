user_input = input().split()

list_of_integers = []
for number in user_input:
    if int(number) >= 0:
        list_of_integers.append(int(number))

list_of_integers.sort()

for i in list_of_integers:
    print(i, end=" ")



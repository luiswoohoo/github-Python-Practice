user_input = int(input())
binary_list = []

while user_input > 0:
    binary_list.append(user_input % 2)
    user_input //= 2

for digit in reversed(binary_list):
    print(digit, end='')

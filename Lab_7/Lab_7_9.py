user_input = input()

tokens = user_input.split()

no_spaces = ''.join(tokens)

reversed_no_spaces = ''
for char in reversed(no_spaces):
    reversed_no_spaces += char

if reversed_no_spaces == no_spaces:
    print('{} is a palindrome'.format(user_input))
else:
    print('{} is not a palindrome'.format(user_input))
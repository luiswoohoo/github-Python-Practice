user_input = input()

words = user_input.split()

uppercase_letters = ''

for word in words:
    if word[0].isupper():
        uppercase_letters += word[0]


print(uppercase_letters)



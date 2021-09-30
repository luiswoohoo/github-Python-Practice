word = input()
password = ''

password_modifier = {
    'i': '1',
    'a': '@',
    'm': 'M',
    'B': '8',
    's': '$'
}

for (index, char_word) in enumerate(word):

    if char_word in password_modifier:
        for char_mod in password_modifier:
            if char_word == char_mod:
                password += password_modifier[char_mod]

    else:
        password += char_word

password += '!'

print(password)
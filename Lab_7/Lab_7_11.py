user_input = input()

alphad_input = ''
for char in user_input:
    if char.islower() == True or char.isupper() == True:
       alphad_input += char

print(alphad_input)
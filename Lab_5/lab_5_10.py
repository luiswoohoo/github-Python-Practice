user_score = 0
simon_pattern = input()
user_pattern = input()

index = 0

for simon_char in simon_pattern:
    if simon_char == user_pattern[index]:
        user_score += 1
        index += 1
        continue
    else:
        break


print('User score:', user_score)
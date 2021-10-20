num_guesses = int(input())
user_guesses = []

num = 0
while num < num_guesses:
    guess = int(input())
    user_guesses.append(guess)
    num += 1

print('user_guesses:', user_guesses)
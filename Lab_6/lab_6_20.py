def steps_to_miles(user_steps):
    miles_walked = user_steps / 2000
    return miles_walked

number_of_steps = int(input())

print('{:.2f}'.format(steps_to_miles(number_of_steps)))
def steps_to_miles(steps):
    if steps < 0:
        raise ValueError('Exception: Negative step count entered.')
    miles = steps / 2000
    return miles


if __name__ == '__main__':
    try:
        input_steps = int(input())
        miles = steps_to_miles(input_steps)
        print('{:.2f}'.format(miles))

    except ValueError as excptn:
        print(excptn)
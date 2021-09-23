is_leap_year = False

input_year = int(input())

# Check if input is a century year
if (input_year > 0) and ((input_year % 100) == 0):
    if (input_year % 400) == 0:
        print(input_year, '- leap year')
    else:
        print(input_year, '- not a leap year')

# If not a century year
elif (input_year > 0) and ((input_year % 100) != 0):
    if (input_year % 4) == 0:
        print(input_year, '- leap year')
    else:
        print(input_year, '- not a leap year')
else:
    print(input_year, '- not a leap year')

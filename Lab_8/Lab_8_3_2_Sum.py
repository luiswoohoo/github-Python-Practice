user_input = input()
test_grades = list(map(int, user_input.split())) # test_grades is an integer list of test scores


sum_extra = 0 # Initialize 0 before your loop

for grade in test_grades:
    if grade > 100:
        sum_extra += (grade - 100)


print('Sum extra:', sum_extra)
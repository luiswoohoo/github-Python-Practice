name = input()
split_name = name.split()

first_name = split_name[0]

if len(split_name) == 2:
    last_name = split_name[1]
    print('{}, {}.'.format(last_name, first_name[0]))
elif len(split_name) == 3:
    middle_name = split_name[1]
    last_name = split_name[2]
    print('{}, {}.{}.'.format(last_name, first_name[0], middle_name[0]))




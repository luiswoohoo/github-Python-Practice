highway_number = int(input())

if (highway_number < 1) or (highway_number > 999) or ((highway_number % 100) == 0):
    print(highway_number, "is not a valid interstate highway number.")

elif (highway_number >= 1) and (highway_number <= 99) and ((highway_number % 2) == 0):
    print('I-{0} is primary, going east/west.'.format(highway_number))

elif (highway_number >= 1) and (highway_number <= 99) and ((highway_number % 2) != 0):
    print('I-{0} is primary, going north/south.'.format(highway_number))

elif (highway_number >= 101) and (highway_number <= 999) and ((highway_number % 2) == 0):
    primary = highway_number % 100

    print('I-{0} is auxiliary, serving I-{1}, going east/west.'.format(highway_number, primary))

elif (highway_number >= 101) and (highway_number <= 999) and ((highway_number % 2) != 0):
    primary = highway_number % 100

    print('I-{0} is auxiliary, serving I-{1}, going north/south.'.format(highway_number, primary))

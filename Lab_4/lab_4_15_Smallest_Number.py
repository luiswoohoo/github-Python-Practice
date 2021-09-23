

first_int = int(input())

second_int = int(input())

third_int = int(input())

if (first_int <= second_int):
    if (first_int <= third_int):
        print(first_int)
    else:
        print(third_int)
else:
    if (second_int <= first_int):
        if (second_int <= third_int):
            print(second_int)
        else:
            print(third_int)
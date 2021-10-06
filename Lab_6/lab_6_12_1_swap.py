def swap(values):
    values.append(values[0])
    values[0] = values[(len(values) - 2)]
    del values[(len(values) - 2)]


values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
swap(values_list)

print(values_list)
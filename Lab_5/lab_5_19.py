number_of_inputs = int(input())

inputs_list = []

for float_input in range(number_of_inputs):
    inputs_list.append(float(input()))

# print(inputs_list)

max_value = -1
for values in inputs_list:
    if values > max_value:
        max_value = values

# print(max_value)

for (index, value) in enumerate(inputs_list):
    inputs_list[index] /= max_value

# print(inputs_list)

for value in inputs_list:
    print('{:.2f}'.format(value))
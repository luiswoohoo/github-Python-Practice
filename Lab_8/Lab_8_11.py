num_resistors = 5
resistors = []
voltage_drop = []

print(f'{num_resistors} resistors are in the series.')
print('This program calculates the'),
print('voltage drop across each resistor.')

input_voltage = float(input('Input voltage applied to circuit: '))

print(f'Input ohms of {num_resistors} resistors')
for i in range(num_resistors):
    res = float(input(f'{i + 1}) '))
    resistors.append(res)

#  Calculate current
current = input_voltage / sum(resistors)

# Calculate voltage drop over each resistor
for resistance in resistors:
    voltage_drop.append(current * resistance)

# Print the voltage drop per resistor
for pos, drop in enumerate(voltage_drop):
    print(f'{pos + 1}) {drop:.1f} V')

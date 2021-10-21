user_input = input()
hourly_temperature = user_input.split()

temperature_reformatted = ''
for temp in hourly_temperature:
    if temp == hourly_temperature[len(hourly_temperature) - 1]:
        temperature_reformatted += (temp + " ")
    else:
        temperature_reformatted += (temp + ' -> ')

print(temperature_reformatted)


def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):
    cost_to_drive = driven_miles * (dollars_per_gallon / miles_per_gallon)

    return cost_to_drive


cars_miles_per_gallon = float(input())
gas_dollars_per_gallon = float(input())

print('{:.2f}'.format(driving_cost(10, cars_miles_per_gallon, gas_dollars_per_gallon)))
print('{:.2f}'.format(driving_cost(50, cars_miles_per_gallon, gas_dollars_per_gallon)))
print('{:.2f}'.format(driving_cost(400, cars_miles_per_gallon, gas_dollars_per_gallon)))
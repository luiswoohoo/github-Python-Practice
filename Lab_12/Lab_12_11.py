class Plant:
    def __init__(self, plant_name, plant_cost):
        self.plant_name = plant_name
        self.plant_cost = plant_cost

    def print_info(self):
        print('Plant Information:')
        print('   Plant name:', self.plant_name)
        print('   Cost:', self.plant_cost)


class Flower(Plant):
    def __init__(self, plant_name, plant_cost, is_annual, color_of_flowers):
        Plant.__init__(self, plant_name, plant_cost)
        self.is_annual = is_annual
        self.color_of_flowers = color_of_flowers

    def print_info(self):
        print('Plant Information:')
        print('   Plant name:', self.plant_name)
        print('   Cost:', self.plant_cost)
        print('   Annual:', self.is_annual)
        print('   Color of flowers:', self.color_of_flowers)


# TODO:  Define the print_list() function that prints a list of plant (or flower) objects
def print_list(plant_list):
    for plant in plant_list:
        plant.print_info()
        print()


if __name__ == "__main__":

    # TODO: Declare a list called my_garden that can hold object of type plant
    my_garden = []

    user_string = input()

    while user_string != '-1':
        # TODO: Check if input is a plant or flower
        #       Split the user_string input into variables - plant_name, plant_cost, color_of_flowers, is_annual
        #       Store as a plant object or flower object
        #       Add to the list my_garden
        input_data = user_string.split()

        if input_data[0] == 'plant':
            plant_name = input_data[1]
            plant_cost = input_data[2]
            my_plant = Plant(plant_name, plant_cost)
            my_garden.append(my_plant)

        if input_data[0] == 'flower':
            plant_name = input_data[1]
            plant_cost = input_data[2]
            is_annual = input_data[3]
            color_of_flowers = input_data[4]
            my_flower = Flower(plant_name, plant_cost, is_annual, color_of_flowers)
            my_garden.append(my_flower)

        user_string = input()


    # TODO: Call the print_list() function to print my_garden
    print_list(my_garden)
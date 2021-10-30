class Car:
    def __init__(self):
        self.model_year = 0
        self.purchase_price = 0
        self.current_value = 0

    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
        # Car depreciation formula
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)

    def print_info(self):
        print('Car\'s information:\n   Model year: {}\n'
              '   Purchase price: {}\n   Current value: {}'
              .format(self.model_year, self.purchase_price, self.current_value))


if __name__ == "__main__":
    user_year = int(input())
    user_price = int(input())
    user_current_year = int(input())

    my_car = Car()
    my_car.model_year = user_year
    my_car.purchase_price = user_price
    my_car.calc_current_value(user_current_year)
    my_car.print_info()

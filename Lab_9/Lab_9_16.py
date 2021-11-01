class VendingMachine:
    def __init__(self):
        self.bottles = 20

    def purchase(self, amount):
        self.bottles = self.bottles - amount

    def restock(self, amount):
        self.bottles = self.bottles + amount

    def get_inventory(self):
        return self.bottles

    def report(self):
        print('Inventory: {} bottles'.format(self.bottles))


if __name__ == "__main__":
# TODO: Create VendingMachine object
    vending_machine = VendingMachine()
# TODO: Purchase input number of drinks
    vending_machine.purchase(int(input()))
# TODO: Restock input number of bottles
    vending_machine.restock(int(input()))
# TODO: Report inventory
    vending_machine.report()
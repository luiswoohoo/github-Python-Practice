class InventoryTag:
    def __init__(self):
        self.item_id = 0
        self.quantity_remaining = 0

red_sweater = InventoryTag()
red_sweater.item_id = int(input())
red_sweater.quantity_remaining = int(input())

''' Your solution goes here '''
print('ID: {}'.format(red_sweater.item_id))
print('Qty: {}'.format(red_sweater.quantity_remaining))
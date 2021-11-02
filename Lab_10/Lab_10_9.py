names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
index = int(input())

# Type your code here.
try:
    print('Name: {}'.format(names[index]))

except IndexError:
    print('Exception! list index out of range')
    if index > 0:
        print('The closest name is: {}'.format(names[len(names) - 1]))
    if index < 0:
        print('The closest name is: {}'.format(names[0]))

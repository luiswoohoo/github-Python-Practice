riders_per_ride = 3  # Num riders per ride to dispatch

line = []  # The line of riders
num_vips = 0  # Track number of VIPs at front of line

menu = ('(1) Reserve place in line.\n'  # Add rider to line
        '(2) Reserve place in VIP line.\n'  # Add VIP
        '(3) Dispatch riders.\n'  # Dispatch next ride car
        '(4) Print riders.\n'
        '(5) What\'s my spot in line?\n'
        '(6) Remove me.\n'
        '(7) Exit.\n\n')

user_input = input(menu).strip().lower()

while user_input != '7':
    if user_input == '1':  # Add rider
        name = input('Enter name:').strip().lower()
        print(name)
        line.append(name)

    elif user_input == '2':  # Add VIP
        # Add new rider behind last VIP in line
        name = input('Enter name:').strip().lower()
        print(name)
        line.insert(num_vips, name)
        num_vips += 1

    elif user_input == '3':  # Dispatch ride
        # Remove last riders_per_ride from front of line.
        # Don't forget to decrease num_vips, if necessary.
        del line[0:3]
        if num_vips > 3:
            num_vips -= 3
        else:
            num_vips = 0

    elif user_input == '4':  # Print riders waiting in line
        print('{} person(s) waiting:'.format(len(line)), line)

    elif user_input == '5':  # Enter a name to find the current position in line
        name = input('Enter name:').strip().lower()
        if name in line:
            print('You are number:' + (str(line.index(name) + 1)))
        else:
            print('That rider isn\'t in the line.')

    elif user_input == '6':  # Enter a name to remove the rider from the line
        name = input('Enter name:').strip().lower()
        if name in line:
            line.remove(name)
        else:
            print('That rider isn\'t in the line.')

    else:
        print('Unknown menu option')

    user_input = input('Enter command: ').strip().lower()
    print(user_input)

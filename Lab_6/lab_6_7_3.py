def print_shampoo_instructions(num_cycles):
    if num_cycles < 2:
        print('Too few.')
    elif num_cycles > 4:
        print('Too many.')
    else:
        n = 1
        while n <= num_cycles:
            print(n, ": Lather and rinse.")
            n += 1
        print('Done.')


user_cycles = int(input())
print_shampoo_instructions(user_cycles)
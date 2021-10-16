mad_lib_input = input()

mad_lib = mad_lib_input.split()
word = mad_lib[0]
number = mad_lib[1]

while word != 'quit':
    print('Eating {} {} a day keeps the doctor away.'.format(number, word))

    mad_lib_input = input()
    mad_lib = mad_lib_input.split()
    word = mad_lib[0]
    number = mad_lib[1]
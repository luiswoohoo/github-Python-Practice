def remove_new_line(contents):
    for i, line in enumerate(contents):
        contents[i] = line.replace('\n', '')


def add_new_line(contents):
    for i, line in enumerate(contents):
        contents[i] = line + '\n'


def output_bounded_list(contents, lower_bound, upper_bound):
    output = []
    for line in contents:
        if lower_bound <= line <= upper_bound:
            output.append(line)
    return output


file_name = input('Enter file name: ')

file = open(file_name)
contents = file.readlines()

file.close()


lower_bound = input('Enter lower bound search term: ')
upper_bound = input('Enter upper bound search term: ')

remove_new_line(contents)
search = output_bounded_list(contents, lower_bound, upper_bound)
# add_new_line(search)

for i in search:
    print(i)






def remove_new_line(contents):
    for i, line in enumerate(contents):
        contents[i] = line.replace('\n', '')


def add_new_line(contents):
    for i, line in enumerate(contents):
        contents[i] = line + '\n'


file_name = input('Enter file name: ')

file = open(file_name)
contents = file.readlines()

file.close()


lower_bound = input('Enter lower bound search term: ')
upper_bound = input('Enter upper bound search term: ')

def output_bounded_list(contents, lower_bound, upper_bound):
    output = []
    for line in contents:
        if lower_bound <= line <= upper_bound:
            output.append(line)
    return output



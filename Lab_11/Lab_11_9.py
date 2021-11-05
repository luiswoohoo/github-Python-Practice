import csv


def convert_csv_to_list(file):
    with open(file, 'r') as csv_file:
        lines = csv.reader(csv_file, delimiter=',')

        return list(lines)[0]


def frequency_calculator(list_of_words):
    frequency_dict = {}
    for word in list_of_words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict


def print_stuff(dict):
    for word, freq in dict.items():
        print('{} {}'.format(word, freq))


input_file = input()

new_list = convert_csv_to_list(input_file)

new_dict = frequency_calculator(new_list)

print_stuff(new_dict)

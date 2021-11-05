input_file = input()


def convert_file_to_list(file):
    with open(file, 'r') as f:
        content = f.readlines()
        for i, line in enumerate(content):
            content[i] = line.replace('\n', '')
        return content


def convert_to_dict(list_of_shows):
    show_dict = {}
    for i in range(0, len(list_of_shows), 2):
        if int(list_of_shows[i]) in show_dict:
            show_dict[int(list_of_shows[i])] += ('; ' + list_of_shows[i + 1])
        else:
            show_dict[int(list_of_shows[i])] = list_of_shows[i + 1]

    return dict(sorted(show_dict.items()))


def write_to_output_keys(sorted_dict):
    with open('output_keys.txt', 'w') as f:
        for seasons, shows in sorted_dict.items():
            f.write('{}: {}\n'.format(seasons, shows))


def write_to_output_titles(shows_list):
    list_of_shows = []
    for i in range(0, len(shows_list), 2):
        list_of_shows.append(shows_list[i + 1])

    with open('output_titles.txt', 'w') as f:
        for show in sorted(list_of_shows):
            f.write('{}\n'.format(show))


new_list = convert_file_to_list(input_file)

# print(new_list)

new_dict = convert_to_dict(new_list)

# print(new_dict)

write_to_output_keys(new_dict)

write_to_output_titles(new_list)

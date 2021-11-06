input_file = input()


def convert_file_to_list(file):
    with open(file, 'r') as f:
        content = f.readlines()
        for i, line in enumerate(content):
            content[i] = line.replace('photo.jpg\n', 'info.txt')
        return content


def print_files(file_list):
    for file in file_list:
        print(file)


contents = convert_file_to_list(input_file)

print_files(contents)

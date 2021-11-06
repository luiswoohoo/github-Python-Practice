def list_builder(file):
    file_name = file + '.txt'
    synonym_list = []
    with open(file_name, 'r') as f:
        content = f.readlines()
        for i, line in enumerate(content):
            content[i] = line.replace('\n', '')

    for words in content:
        synonym_list.append(words.split(' '))
    return synonym_list


def thesaurus_builder(synonyms):
    synonyms_dict = {}
    for words in synonyms:
        synonyms_dict[words[0][0]] = words
    return synonyms_dict


def print_synonyms(file, letter, thesaurus):
    if letter in thesaurus:
        for word in thesaurus[letter]:
            print(word)
        # print(thesaurus[letter])
    else:
        print('No synonyms for {} begin with {}.'.format(file, letter))


file_input = input()
letter_input = input()

synonyms_list = list_builder(file_input)
# print(synonyms_list)

new_dict = thesaurus_builder(synonyms_list)
# print(new_dict)

print_synonyms(file_input, letter_input, new_dict)
#test
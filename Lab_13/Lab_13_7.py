def all_permutations(permList, nameList):

    if len(nameList) == 0:
        names_to_print = ''
        for name in permList:
            names_to_print += (name + ' ')
        print(names_to_print)

    else:
        for i in range(len(nameList)):
            names = nameList[:]
            removed_name = names[i]
            names.pop(i)
            permList.append(removed_name)
            all_permutations(permList, names)
            permList.pop()


if __name__ == "__main__":
    nameList = input().split(' ')
    permList = []
    all_permutations(permList, nameList)

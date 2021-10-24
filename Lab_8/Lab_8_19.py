contacts_list = input().split()
contact = input()

for pos, i in enumerate(contacts_list):
    if i == contact:
        print(contacts_list[pos + 1])

integer1 = int(input())
integer2 = int(input())

if integer2 < integer1:
    print("Second integer can't be less than the first.", end='')

else:
    for integer in range(integer1, integer2 + 1, 5):
        print(integer, end=" ")

print()
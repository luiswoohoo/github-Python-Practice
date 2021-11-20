def digit_count(n):
    if 0 <= n < 10:
        return 1
    else:
        return 1 + digit_count(n//10)


if __name__ == '__main__':
    num = int(input())
    digit = digit_count(num)
    print(digit)

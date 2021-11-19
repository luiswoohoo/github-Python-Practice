def fibonacci(n):
    if n < 0:
        return -1

    if n == 0 or n == 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    start_num = int(input())
    print('fibonacci({}) is {}'.format(start_num, fibonacci(start_num)))

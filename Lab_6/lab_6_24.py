def fibonacci(n):
    fibonacci_list = [0, 1]

    if n < 0:
        return -1

    if n >= 0:
        i = 0
        while i <= n:
            next = fibonacci_list[i + 1] + fibonacci_list[i]
            fibonacci_list.append(next)
            i += 1

        return fibonacci_list[n]


start_num = int(input())
print('fibonacci({}) is {}'.format(start_num, fibonacci(start_num)))
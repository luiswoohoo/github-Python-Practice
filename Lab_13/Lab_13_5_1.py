from functools import lru_cache


@lru_cache
def compute_nth_fib(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    if num >= 2:
        fib = compute_nth_fib(num - 1) + compute_nth_fib(num - 2)
        return fib

fib_num = int(input())
print(compute_nth_fib(fib_num))

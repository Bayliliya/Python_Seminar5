"""Последовательностью Фибоначчи называется последовательность
чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи"""


# My use for
def fib_for(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return a


print(fib_for(10))

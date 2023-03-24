"""Последовательностью Фибоначчи называется последовательность
чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи"""

# # My use for
# def fib_for(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b

#     return a

# k = 2
# print(fib_for(k))

# # My - FIX ERROR
# def fib_rec(n):
#     if n <= 1:
#         return n
#     else:
#         return fib_rec(n - 1) + fib_rec(n - 2)

# print(fib_rec(3))

# My - Memo
cahce = {}


def fib_rec_cache(n):
    if n not in cahce:
        cahce[n] = n if n <= 1 else fib_rec_cache(n - 1) + fib_rec_cache(n - 2)
    return cahce[n]


print(fib_rec_cache(100))

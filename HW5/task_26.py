'''Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
'''


def rekurs_a_ext_b(a, b):
    """Рекурсивная функция нахождения A в степени B"""
    if b == 0:
        return 1
    return a * rekurs_a_ext_b(a, b - 1)


n = int(input("N: "))
m = int(input("M: "))

print(rekurs_a_ext_b(n, m))

'''Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
'''


def rekurs_A_ext_B(A, B):
    """Рекурсивная функция нахождения A в степени B"""
    if B == 0:
        return 1
    return A * rekurs_A_ext_B(A, B - 1)


N = int(input("N: "))
M = int(input("M: "))

print(rekurs_A_ext_B(N, M))

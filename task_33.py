'''Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные
'''

import random

count_grade_book = int(input("Введите количество оценок: "))
grade_book = []
for _ in range(count_grade_book):
    grade_book.append(random.randint(1, 5))
print(grade_book)


def return_max_min(numbers):
    """Функция для нахождения максимума и минимума"""
    max_num = float("-inf")
    min_num = float("inf")
    for j in numbers:
        if j > max_num:
            max_num = j
        elif j < min_num:
            min_num = j
    return min_num, max_num


def replace_max_min(numbers):
    """Функция заменяет максимальные значения на минимальные"""
    min_grade, max_grade = return_max_min(numbers)
    for i, num in enumerate(numbers):
        if num == max_grade:
            numbers[i] = min_grade
    return numbers


print(replace_max_min(grade_book))

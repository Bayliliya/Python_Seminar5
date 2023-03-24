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


def reverse_grade_book():
    """Функция для нахождения максимума и минимума"""
    max_grade = float("-inf")
    min_grade = float("inf")
    for j in grade_book:
        if j > max_grade:
            max_grade = j
        elif j < min_grade:
            min_grade = j
    return [min_grade, max_grade]


min_grade_reverse = reverse_grade_book()[0]
max_grade_reverse = reverse_grade_book()[1]

grade_book_revers = []

for i in grade_book:
    if i == max_grade_reverse:
        i = min_grade_reverse
        grade_book_revers.append(i)
    else:
        grade_book_revers.append(i)

print(grade_book_revers)

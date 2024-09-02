"""
1. Написать программу, которая будет выводить на экран числа Фибоначчи до заданного числа.
"""


def print_fib(n: int) -> None:
    fib1, fib2 = 0, 1
    fib = 0
    if n == 1: print(fib1)
    if n == 2: print(fib1, fib2)
    while fib != n:
        fib = fib1 + fib2
        print(fib1, end=' ')
        fib1, fib2 = fib, fib1
        if fib > n:
            break


print_fib(16)
print('\n -------------------- ')
"""
2. Напишите программу, которая на вход принимает список чисел
 и возвращает только уникальные значения из этого списка.
"""


def get_unique(lst: list) -> list:
    unique_list = []
    for elem in lst:
        if elem not in unique_list:
            unique_list.append(elem)
    return unique_list


lst = [1, 1, 5, 3, 11, 5]
print(get_unique(lst))

"""
3. Напишите программу, которая переводит температуру в градусах Фаренгейта в градусы Цельсия.
"""


def transform_t(n: int) -> float:
    return round((n - 32) * 5 / 9, 2)


print(transform_t(35))
"""
4. Напишите программу, которая проверяет, является ли строка палиндромом без использования стандартных методов.
"""


def is_palindrom(s: str) -> bool:
    s = s.replace(' ', '')
    return s == s[::-1]


def is_palindrom_v1(s: str) -> bool:
    new_s = ''
    s = ''.join(s.split())
    for i in range(len(s) - 1, -1, -1):
        new_s += s[i]
    return s == new_s


s = 'она не жена но'
print(is_palindrom(s))
print(is_palindrom_v1(s))

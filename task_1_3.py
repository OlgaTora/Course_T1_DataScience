"""
1.Напишите программу, которая будет выводить на экран площадь квадрата и его периметр.
Сторона квадрата будет равна 25.
"""


def get_square(size):
    return size ** 2, size * 4


print(get_square(25))

"""
2. Напишите функцию, которая будет принимать два числа и считать сумму квадратов этих двух
чисел, запишите своё вычисление в переменную squared. 
"""


def get_sum_squares(n, m):
    squared = n ** 2 + m ** 2
    return squared

"""
3. Напишите функцию, которая будет принимать на вход список [“male“,“male“,“female“,“male“,“male“,“female“,”female“] 
и возвращать его в обратном порядке. Запишите список в переменную new_list. 
"""


def reverse_list(lst) -> list:
    return lst[::-1]


new_list = reverse_list(['male', 'male', 'female', 'male', 'male', 'female', 'female'])

"""
4.Напишите функцию, которая будет принимать на вход список (new_list) и идти по нему в цикле.
На выходе функция должна вывести на экран: Кол-во мужчин 4, Кол-во женщин 3.
"""


def print_list(lst: list) -> None:
    male, female = 0, 0
    for i in lst:
        if i == 'male':
            male += 1
        else:
            female += 1
    print(f'Кол-во мужчин {male}, Кол-во женщин {female}.')


print_list(new_list)

"""
5. Напишите функцию, которая будет принимать строку (Например: “female”),
а возвращать словарь где ключи — это символы строки, а значения кол-во символов в строке. 
"""


def str2dict(s: str) -> dict:
    dct = {}
    for letter in s:
        dct[letter] = dct.get(letter, 0) + 1
    return dct


"""
6.Воспользуйтесь функцией range в Python и выведите на экран сумму квадратов от 1 до 100 (включительно). 
"""

print(sum([i ** 2 for i in range(1, 101)]))

"""
7. Укажите какой метод добавит значение в конец списка. Приведите пример.
"""

lst = [1, 2, 3]
lst.append('e')
print(lst)

"""
8. Как объединить два списка "a" и "b" в один новый список "c"? Приведите пример.
"""
lst1 = [1, 2]
lst2 = ['a', 5]
res = lst1 + lst2
print(res)

"""
9. Укажите какой метод посчитает количество значений в списке. Приведите пример.
"""

print(len(res))

"""
10. 
"""
x = 2 ** 4
y = 4 ** 2
if x < y:
    print("x меньше y")
else:
    print("x больше, либо равен y")

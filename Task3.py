
"""Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 39"""

n = input("Введите целое число n: ")
result = int(n) + (int(n) * int(n)) + (int(n) * int(n) * int(n))
print(result)

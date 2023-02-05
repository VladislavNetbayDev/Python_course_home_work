"""1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

*Пример:*

- 6 -> да
- 7 -> да
- 1 -> нет"""
number_of_week = input("Введите цифру дня недели: ")
number_of_week = int(number_of_week)
if(number_of_week > 0 and number_of_week < 8):
    if(number_of_week > 0 and number_of_week < 6):
        print("no")
    else: print("yes")
else: print("Число не отражает день недели")


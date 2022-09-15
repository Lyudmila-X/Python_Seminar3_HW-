# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

import math
n = int(input('Введите кол-во чисел, которые вы собираетесь ввести: '))
print ('Введите вещественные числа: ')
newlist = list()
for i in range(n):
    newlist.append(float(input()))
print (newlist)
secondlist = list()
for i in newlist:
    secondlist.append(i%1)
print (max(secondlist)-min(secondlist))

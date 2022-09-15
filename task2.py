# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.

from task1 import list_input
import math
numlist = list_input()
for i in range(math.ceil(len(numlist)/2)):
    print (numlist[i]*numlist[-(i+1)])

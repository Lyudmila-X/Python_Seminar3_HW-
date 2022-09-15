# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

def list_input ():
    n = int(input('Введите кол-во чисел, которые вы собираетесь ввести: '))
    print ('Введите числа: ')
    newlist = list()
    for i in range(n):
        newlist.append(int(input()))
    return newlist
if __name__ == '__main__':
    sum = 0
    numlist = list_input()
    for i in range(1, len(numlist), 2):
        sum+=numlist[i]
    print (sum)

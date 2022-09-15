# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

n = int(input("Введите число: "))
binnum = ''
if n==0:
    print (0)
else:
    while n > 0:
        binnum = str(n % 2) + binnum
        n = n // 2
    print(binnum)

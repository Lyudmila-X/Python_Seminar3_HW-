# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Доп)

n = int(input("Введите число N: "))
def fib (n):
    if n in range(1, 3):
        return 1
    return (fib (n - 1) + fib (n - 2))
def negofib (n):
    if n==-1:
        return 1
    elif n==-2:
        return -1
    return (negofib (n + 2) - negofib (n + 1))
for i in range(-n, n+1):
    if i<0:
        print(negofib(i), end=" ")
    elif i==0:
        print(0, end=" ")
    elif i>0:
        print(fib(i), end=" ")


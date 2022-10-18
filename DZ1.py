# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

N = int(input('Введите число: '))


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


list = []
for e in range(1, N+1):
    list.append(fib(e))

data = open('fibo.txt', 'w')
data.write(str(list))
data.close()

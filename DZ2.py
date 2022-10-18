# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

letterN = input('Введите букву: ')
#letter = ''
path = 'frukt.txt'
data = open(path, 'r')
for line in data:
    #letter = line
    if letterN == line[0]:
        print(line)
data.close()
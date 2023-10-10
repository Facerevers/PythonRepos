# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

import random
coins = int(input('Введите количество монеток: '))
rand_list = []
for i in range(coins):
    rand_list.append(random.randint(0, 1))
print(rand_list)
countofheads, countoftails = 0, 0
for i in rand_list:
    if i == 1:
        countofheads += 1
    elif i == 0:
        countoftails += 1
if countofheads >= countoftails:
    print(countoftails)
else:
    print(countofheads)

# ==========
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму
# этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

summa = int(input('Введите сумму двух чисел: '))
product = int(input('Введите произведение двух чисел: '))
firstnum = ((-1 * summa) - ((summa ** 2) - (4 * -1 * (-1 * product))) ** 0.5)/ -2
secondnum = summa - firstnum
print(firstnum, secondnum)

# ===========
# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите число N: '))
i = 1
lst = []
while i <= n:
    lst.append(i)
    i *= 2
print(lst)
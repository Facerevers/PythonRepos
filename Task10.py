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
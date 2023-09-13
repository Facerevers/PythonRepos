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
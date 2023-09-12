summa = int(input('Введите сумму двух чисел: '))
product = int(input('Введите произведение двух чисел: '))
firstnum = ((-1 * summa) - ((summa ** 2) - (4 * -1 * (-1 * product))) ** 0.5)/ -2
secondnum = summa - firstnum
print(firstnum, secondnum)
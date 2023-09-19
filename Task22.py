n = int(input(' Введите количество элементов первого множества: '))
m = int(input(' Введите количество элементов второго множества: '))
list_1 = input('Введите элементы первого множества через пробел: ')
list_2 = input('Введите элементы второго множества через пробел: ')
lst1 = list_1.split()
lst2 = list_2.split()
first_mn = []
second_mn = []
for i in lst1:
    first_mn.append(i)
for i in lst2:
    second_mn.append(i)
fst = set(first_mn)
scnd = set(second_mn)
out_mn = fst.intersection(scnd)
print(sorted(out_mn))
n = int(input(' Введите количество элементов первого множества: '))
m = int(input(' Введите количество элементов второго множества: '))
list_1 = input('Введите элементы первого множества через пробел: ')
list_2 = input('Введите элементы второго множества через пробел: ')
lst1 = list_1.split()
lst2 = list_2.split()
first_mn = []
second_mn = []
i = 0
j = 0
while i < n:
    first_mn.append(lst1[i])
    i += 1
print(first_mn)
while j < m:
    second_mn.append(lst2[j])
    j += 1
print(second_mn)
fst = set(first_mn)
scnd = set(second_mn)
out_mn = fst.intersection(scnd)
print(sorted(out_mn))
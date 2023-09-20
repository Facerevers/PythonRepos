"""Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств."""

first_mn = list(map(int, input("Введите элементы первого множества: ").split(" ")))
second_mn = list(map(int, input("Введите элементы второго множества: ").split(" ")))
fst = set(first_mn)
scnd = set(second_mn)
out_mn = fst.intersection(scnd)
print(sorted(out_mn))
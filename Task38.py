"""Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной
записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной"""
import os.path

def users_commands(phonebook):
    while True:
        print('Телефонный справочник\n\n1 - Просмотреть все контакты\n2 - Найти контакт\n3 - Добавить контакт\n4 - Изменить контакт\n5 - удалить контакт\n6 - Выйти из приложения\n')
        users_choice = input('Выберите нужное вам действие: ')
        if users_choice == '1':
            print_contacts(phonebook)
        elif users_choice == '2':
            list_of_contacts == read_file(phonebook)
            find_contact(list_of_contacts)
        elif users_choice == '3':
            add_new_contact(phonebook)
        elif users_choice == '4':
            change_contact(phonebook)
        elif users_choice == '5':
            delete_contact(phonebook)
        elif users_choice == '6':
            print('Выход')
            break
        else:
            print('Такой команды нет. Please, change the user and try again')
            print()
            continue

def print_contacts(file_name):
    contact_list = sorted(read_file(file_name))
    print_contacts(contact_list)
    print()
    return contact_list

def find_param():
    print('По какому полю ищем?\n\n1 - По фамилии\n2 - По имени\n3 - По отчеству\n4 - По номеру телефона\n5 - Выйти')
    print()
    first_param = input('Введите номер поля, по которому будем искать абонента')
    second_param = None
    while True:
        if first_param == '1':
            second_param = input('Введите фамилию: ')
            print()
            break
        elif first_param == '2':
            second_param = input('Введите имя: ')
            print()
            break
        elif first_param == '3':
            second_param = input('Введите отчество: ')
            print()
            break
        elif first_param == '4':
            second_param = input('Введите номер телефона: ')
            print()
            break
        elif first_param == '5':
            print()
            break
        else:
            print('Такого поля нет, выберите корректное поле')
            print()
            continue
    return first_param, second_param

def find_contact(list_of_contacts):
    first_param, second_param = find_param()
    if first_param == 5:
        print('Вы передумали искать')
        return
    found_contacts = []
    for i in range(len(list_of_contacts)):
        new_list = list(list_of_contacts[i])
        if new_list[int(first_param) - 1] == second_param:
            found_contacts.append(new_list)
    if len(found_contacts) == 0:
        print('Такого абонента нет')
    else:
        print_contact(found_contacts)

def add_new_person():
    second_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    third_name = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    return second_name, first_name, third_name, phone

def add_new_contact(file_name):
    info = ' '.join(add_new_person())
    with open(file_name, 'a', encoding = 'utf-8') as file:
        file.write(f'{info}\n')
    print()

def change_contact(file_name):
    list_of_contacts = sorted(list(read_file(file_name)))
    print_contact(list_of_contacts)
    contact_number = int(input('Введите номер контакта, который хотите изменить (0 - Отмена операции)'))
    if contact_number == 0 or len(list_of_contacts) < contact_number:
        print('Контакта с таким номером нет в базе')
        print(contact_number, len(list_of_contacts))
        return
    print()
    print(f'Меняем абонента - {list_of_contacts[contact_number - 1]}')
    new_list = list(list_of_contacts[contact_number - 1])
    print('Изменение контакта\n1 - Фамилия\n2 - Имя\n3 - Отчество\n4 - Телефон\n5 - Отмена')
    print()
    choice = input('Введите номер поля, который вы будете менять у контакта: ')
    if choice == '1':
        change = input('Введите новую фамилию: ')
    elif choice == '2':
        change = input('Введите новое имя: ')
    elif choice == '3':
        change = input('Введите новое отчество: ')
    elif choice == '4':
        change = input('Введите новый номер телефона: ')
    elif choice == '5':
        print()
        return
    new_list[int(choice) - 1] = change
    list_of_contacts[contact_number - 1] = new_list
    with open(file_name, 'w', encoding = 'utf-8') as file:
        for contact in list_of_contacts:
            line = ' '.join(contact) + '\n'
            file.write(line)
    print()
    print('Изменённый справочник')
    print_contacts(file_name)

def delete_contact(file_name):
    list_of_contacts = sorted(list(read_file(file_name)))
    print_contact(list_of_contacts)
    contact_number = int(input(' Введите номер контакта, который хотите удалить (0 - для отмены)'))
    if contact_number == 0 or len(list_of_contacts) < contact_number:
        print('Абонента с таким ноером нет')
        print()
        return
    list_of_contacts.pop(contact_number - 1)
    with open(file_name, 'w', encoding = 'utf-8') as file:
        for contact in list_of_contacts:
            line = ' '.join(contact) + '\n'
            file.write(line)
    print()

def read_file(file_name):
    with open(file_name, 'r', encoding = 'utf-8') as file:
        list_of_contact = []
        for line in file.readlines():
            list_of_contact.append(line.split())
    return list_of_contact

def print_contact(list_of_contact):
    for i in range(len(list_of_contact)):
        outlist = list(list_of_contact[i])
        print("{:<4}".format(i + 1), "{:<12}".format(outlist[0]), "{:<12}".format(outlist[1]), "{:<12}".format(outlist[2]), "{:<12}".format(outlist[3]))
    print()

file_name = 'Phonebook.txt'
if not os.path.isfile(file_name):
    with open(file_name, 'w', encoding = 'utf-8') as data:
        data.write(' Фамилия Имя Отчество Телефон\n')
users_commands(file_name)
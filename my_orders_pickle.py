"""
Программа для сохранения покупок
Название + Цена
"""
import os
import pickle

FILE_NAME = 'history'
schet = 'schet'
files = 'listdir.txt'


orders = []
num = []
file = os.listdir()

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'rb') as f:
        orders = pickle.load(f)

if os.path.exists(schet):
    with open(schet, 'rb') as f:
        num = pickle.load(f)

while True:
    print('Мой банковский счет :',num)
    print('1. Добавить покупку')
    print('2. История покупок')
    print('3. Изменить сумму счета')
    print('4. Просмотр содержимого рабочей дериктории')
    print('5. Сохранить содержимое рабочей директории в файл')
    print('6. Выход')
    choise = input('Введите номер: ')
    if choise == '1':
        name = input('Введите название: ')
        cost = int(input('Введите цену: '))
        order = (name, cost)
        orders.append(order)
    elif choise == '2':
        for order in orders:
            print(order)
    elif choise == '3':
        cod = input('Изменим сумму счета:')
        num = cod
        print(num)
    elif choise == '4':
        for i in file:
         print(i)
    elif choise == '5':
        with open(files,'wb') as f:
            pickle.dump(file,f)
    elif choise == '6':
        with open(FILE_NAME, 'wb') as f:
            pickle.dump(orders, f)
        with open(schet, 'wb') as f:
            pickle.dump(num, f)
        break
    else:
        print('Неправильно введены даные')

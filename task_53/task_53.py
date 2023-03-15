# Создать телефонный справочник с возможностью импорта и
# экспорта данных в формате .txt. Фамилия, имя, отчество,
# номер телефона - данные, которые должны находиться в файле.

# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска
# определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

def show_data():
    """Функция показывает содержимое справочника"""
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read()
    print(book.replace(';', ' '))


def new_data(info: str):
    """Функция добавляет новую информацию в справочник"""
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(';'.join(info[1:]) + '\n')
        print('Запись добавлена')


def search_data(data: str):
    """Функция ищет записи в справочнике"""
    with open('data.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if data.lower() in line.lower():
                print(line.replace(';', ' '))


def delete_data(data: str):
    """Функция удаляет запись в справочнике"""
    temp = ''
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = tuple(file.read().split('\n'))
        for line in book:
            if data.lower() not in line.lower():
                temp += line + '\n'
            else:
                print('Запись удалена')
    with open('data.txt', 'w', encoding='utf-8') as file:
        file.write(temp)


def change_data(data: str):
    """Функция редактирует запись в справочнике"""
    temp = ''
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = tuple(file.read().split('\n'))
        for line in book:
            if data.lower() not in line.lower():
                temp += line + '\n'
            else:
                print(f"Найдена запись: {line.replace(';', ' ')}")
                inp = input('Введите новую запись: ').split()
                temp += ';'.join(inp) + '\n'
                print('Запись изменена')
    with open('data.txt', 'w', encoding='utf-8') as file:
        file.write(temp)


def menu():
    """Функция печатает меню"""
    print('Выберите режим работы справочника:\n"show" для вывода'
          ' содержимого справочника на экран\n"new ФИО телефон" для '
          'внесения новой записи\n"search ФИО и/или телефон '
          'для поиска записи\n"delete ФИО и/или телефон" для удаления записи\n'
          '"change ФИО и/или телефон" для его редактирования\n'
          '"exit" для выхода\n')


print('Приветствую тебя в телефонном справочнике')
menu()
while True:
    mode = tuple(input('Введите команду: ').split())
    if mode[0] == 'show':
        show_data()
    elif mode[0] == 'new':
        new_data(mode)
    elif mode[0] == 'search':
        search_data(mode[1])
    elif mode == "menu":
        menu()
    elif mode[0] == 'delete':
        delete_data(mode[1])
    elif mode[0] == 'change':
        change_data(mode[1])
    elif mode == 'exit':
        break

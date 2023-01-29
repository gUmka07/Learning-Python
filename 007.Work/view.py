"""Модуль ввода и вывода информации"""


def main_menu():
    """Вывод главного меню в консоль"""
    menu_list = [
        'Открыть справочник',
        'Показать все контакты',
        'Найти контакт',
        'Создать контакт',
        'Изменить контакт',
        'Удалить контакт',
        'Сохранить изменения',
        'Выход'
    ]
    print('\nГлавное меню')
    for i, value in enumerate(menu_list, start=1):
        print(f'\t{i}. {value}')
    print()


def user_input(contacts: list):
    """
    Функция обработки пользовательского ввода.
    :return: номер команды для дальнейшей работы программы.
    """
    while True:
        try:
            main_menu()
            command = int(input('Введите номер команды -> '))
            if command < 1 or command > 8:
                print('\nВы ввели {command}! Введите номер команды от 1 до 7.\n')
            elif contacts and command == 1:
                print('\nТелефонный справочник уже открыт!')
            else:
                return command
        except ValueError:
            print('\nНекорректный ввод! Введите номер команды.\n')


def show_all_contacts(contacts: list):
    """Вывод списка всех контактов в консоль"""
    print('\nСписок контактов:')
    for i, item in enumerate(contacts):
        print(f'\t{i + 1}.', end=' ')
        for value in item.values():
            print(f'{value}', end=' ')
        print()


def create_contact(contacts: list):
    """Создание нового контакта"""
    print('\nВведите данные контакта:')
    new_contact = {'ID': 'id_' + str(len(contacts) + 1), 'Lastname': input('\tФамилия: '),
                   'Firstname': input('\tИмя: '), 'phone': input('\tНомер телефона: '),
                   'Comment': input('\tКомментарий: ')}
    print('\nКонтакт добавлен. Вы можете сохранить изменения сейчас или позже.')
    return new_contact


def find_choice() -> tuple:
    """
    Функция выбора критерия поиска контакта и значения для поиска.
    :return: номер критерия, значение для поиска.
    """
    print('\nКритерии поиска:')
    find_list = [
        'Фамилия',
        'Имя',
        'Фамилия и имя',
        'Номер телефона',
        'ID контакта (численное значение)'
    ]

    for i, value in enumerate(find_list, start=1):
        print(f'\t{i}. {value}')
    print()

    while True:
        try:
            user_choice = int(input('Выберите номер критерия поиска: '))
            if user_choice < 1 or user_choice > 5:
                print('\nВведите номер команды от 1 до 4.\n')
            else:
                find_data = input('Введите данные для поиска в соответствии с критерием: ')
                if user_choice < 5:
                    return user_choice, find_data
                if user_choice == 5 and find_data.isdigit():
                    find_data = 'id_' + str(find_data)
                    return user_choice, find_data
                if user_choice == 5 and not find_data.isdigit():
                    print('\nНекорректный ID! Необходимо вводить только число ID. '
                          'Вы можете изменить критерий поиска.\n')
        except ValueError:
            print('\nНекорректный ввод! Введите номер команды.\n')


def show_contact(contacts: list):
    """
    Вывод контакта в консоль.
    :param contacts: список контактов.
    """
    print('\nКонтакт(ы): ')
    if contacts:
        for i, item in enumerate(contacts):
            print(f'\t{i + 1}', end=' ')
            print(f'{" ".join(item.values())}')
    else:
        print('\tКонтакт не найден!\n')


def change_contact(contacts: list):
    """
        Изменение контакта. Осуществляется по ID контакта.
        :param contacts: список контактов
        """
    print('\nИзменение контакта.\nДля исключения потери информации изменение '
          'контакта осуществляется по ID контакта.\nЕсли вы не знаете ID контакта, выберите '
          'команду в главном меню "Найти контакт" или "Показать все контакты".'
          '\nДля отмены изменения выберите "ОТМЕНА"\n')
    print('1. Ввести ID\n2. ОТМЕНА')

    while True:
        try:
            command = int(input('Введите номер команды: '))
            if command < 1 or command > 2:
                print('\nВведите номер команды (1 или 2).\n')
            else:
                match command:
                    case 1:
                        id_contact = input('Введите ID: ')
                        if id_contact.isdigit() and 1 <= int(id_contact) <= len(contacts):
                            print(f'\nИзмените данные контакта: id_{id_contact} '
                                  f'{contacts[int(id_contact) - 1]["Lastname"]} '
                                  f'{contacts[int(id_contact) - 1]["Firstname"]} '
                                  f'{contacts[int(id_contact) - 1]["phone"]} '
                                  f'{contacts[int(id_contact) - 1]["Comment"]}:\n')
                            new_contact = {'ID': 'id_' + id_contact,
                                           'Lastname': input('\tФамилия: '),
                                           'Firstname': input('\tИмя: '),
                                           'phone': input('\tНомер телефона: '),
                                           'Comment': input('\tКомментарий: ')}
                            print('\nКонтакт изменен.\nДля сохранения изменений в файле выберите '
                                  '"Сохранить изменения" в главном меню.')
                            return int(id_contact), new_contact
                        if not id_contact.isdigit() or int(id_contact) < 1 or \
                                int(id_contact) > len(contacts):
                            print('\nID введен некорректно или отсутствует!\n'
                                  'Для изменения контакта выберите'
                                  ' необходимую команду в главном меню.')
                            return None
                    case 2:
                        print('\nИзменение отменено\n')
                        return None
        except ValueError:
            print('\nНекорректный ввод! Введите номер команды\n')


def delete_contact(contacts: list):
    """
    Удаление контакта. Осуществляется по ID контакта.
    :param contacts: список контактов
    """
    print('\nУдаление контакта.\nДля исключения потери информации удаление '
          'контакта осуществляется по ID контакта.\nЕсли вы не знаете ID контакта, выберите '
          'команду в главном меню "Найти контакт" или "Показать все контакты".'
          '\nДля отмены удаления выберите "ОТМЕНА"\n')
    print('\n1. Ввести ID\n2. ОТМЕНА')

    while True:
        try:
            command = int(input('Введите номер команды: '))
            if command < 1 or command > 2:
                print('\nВведите номер команды (1 или 2).\n')
            else:
                match command:
                    case 1:
                        id_contact: str = input('Введите ID: ')
                        if id_contact.isdigit() and 1 <= int(id_contact) <= len(contacts):
                            contact = ' '.join(contacts[int(id_contact) - 1].values())
                            print(f'\nКонтакт "{contact}" удален.\nID контактов обновлены.\n'
                                  'Для сохранения изменений выберите "Cохранить изменения" '
                                  'в главном меню.')
                            return id_contact
                        if not id_contact.isdigit() or int(id_contact) < 1 or \
                                int(id_contact) > len(contacts):
                            print('\nID введен некорректно или отсутствует!\n'
                                  'Для удаление контакта выберите необходимую команду.')
                            return None
                    case 2:
                        print('\nУдаление отменено\n')
                        return None
        except ValueError:
            print('\nНекорректный ввод! Введите номер команды\n')


def question_yes_no(question: str, answer_yes: str, answer_no: str):
    """
    Функция обработки ответа пользователя ДА или НЕТ
    :param question: вопрос.
    :param answer_yes: ответ программы на ответ 'да' от пользователя.
    :param answer_no: ответ программы на ответ 'нет' от пользователя.
    :return: True или False
    """
    print(question)
    while True:
        user_inp = input('Введите ДА или НЕТ: ')
        if user_inp.lower() not in ['да', 'нет']:
            print('\nНекорректный ввод! Введите ДА или НЕТ.\n')
        if user_inp.lower() == 'да':
            print(answer_yes)
            return True
        if user_inp.lower() == 'нет':
            print(answer_no)
            return False


def save_answer() -> bool:
    """Сохранение изменений"""
    print('\nСохранение изменений.\n')
    question = 'Сохранить изменения?'
    answer_yes = 'Изменения сохранены'
    answer_no = 'Изменения не сохранены'
    return question_yes_no(question, answer_yes, answer_no)


def exit_answer() -> bool:
    """Завершение работы программы."""
    print('\nЗавершение работы программы.\n')
    question = 'Завершить работу программы?'
    answer_yes = 'Работа программы завершена.'
    answer_no = 'Работа программы не завершена.'
    return question_yes_no(question, answer_yes, answer_no)


def show_message(text: str):
    """Вывести сообщение пользователю в консоль"""
    print(text)
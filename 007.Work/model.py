"""Модуль-модель: предоставление данных"""
contacts_list: list = []
state: bool = False


def get_db() -> list:
    """Возврат списка контактов"""
    return contacts_list


def add_in_contacts(new_contact: dict) -> list:
    """Добавление элемента в список контактов"""
    contacts_list.append(new_contact)
    return contacts_list


def save_in_db(path: str, new_contact: dict):
    """
    Добавление в файл контакта.
    :param path: путь файла.
    :param new_contact: словарь контакта.
    """
    contact = ''
    if len(contacts_list) == 1:
        contact = ';'.join(new_contact.values())
    elif len(contacts_list) > 1:
        contact = ';'.join(new_contact.values())
        contact = '\n' + contact
    with open(path, 'a', encoding='UTF-8') as data:
        data.write(contact)


def read_db(path: str):
    """
    Функция чтения информации из базы данных (файла) и формирования списка словарей.
    :param path: файл с контактами.
    """
    global state
    state = True
    with open(path, 'r', encoding='UTF-8') as data:
        data_list = data.readlines()
        for line in data_list:
            contact_info = line.strip().split(';')
            key_info = ['ID', 'Lastname', 'Firstname', 'phone', 'Comment']
            dict_contact = dict(zip(key_info, contact_info))
            add_in_contacts(dict_contact)


def rewrite_db(path: str, new_contacts: list):
    """
    Перезаписать данные в файле.
    :param path: путь/имя файла для перезаписи.
    :param new_contacts: список с измененными данными.
    """
    new_data = []
    for item in new_contacts:
        contact = ';'.join(item.values())
        contact += '\n'
        new_data.append(contact)
    with open(path, 'w', encoding='UTF-8') as data:
        for item in new_data:
            data.write(item)


def delete_in_db(id_contact: str) -> list:
    """
    Удаление контакта.
    :param id_contact: id контакта.
    :return: обновленный лист контактов.
    """
    contacts_list.pop(int(id_contact) - 1)
    for i, value in enumerate(contacts_list):
        value['ID'] = 'id_' + str(i + 1)
    return contacts_list


def change_contact(change_data: tuple) -> list:
    """
    Изменение контакта.
    :param change_data: кортеж с id контакта(int) и измененные данные(словарь).
    :return: обновленный список контактов.
    """
    i = change_data[0] - 1
    new_contact = change_data[1]
    contacts_list[i]['Lastname'] = new_contact['Lastname']
    contacts_list[i]['Firstname'] = new_contact['Firstname']
    contacts_list[i]['phone'] = new_contact['phone']
    contacts_list[i]['Comment'] = new_contact['Comment']
    return contacts_list


def found_contacts(find_choice: tuple) -> list:
    """
    Поиск контакта в списке контактов.
    :param find_choice: кортеж: критерий поиска и данные для поиска.
    :return: список контактов.
    """

    def find() -> list:
        """Внутрення функция поиска для однотипных запросов, исключающая повторение кода.
        :rtype: object
        """
        keys = ['Lastname', 'Firstname', 'Lastname_firstname', 'phone', 'ID']
        found: list = []
        for value in contacts_list:
            if find_choice[1].lower() == value[keys[find_choice[0] - 1]].lower():
                found.append(value)
        return found

    match find_choice[0]:
        case 1:
            new_found: list = find()
            return new_found
        case 2:
            new_found: list = find()
            return new_found
        case 3:
            new_found: list = []
            find = list(find_choice[1].lower().split())
            if len(find) == 1:
                return new_found
            if len(find) == 2:
                for item in contacts_list:
                    if find[0] == item['Lastname'].lower() and \
                            find[1] == item['Firstname'].lower():
                        new_found.append(item)
                return new_found
        case 4:
            new_found: list = find()
            return new_found
        case 5:
            new_found: list = find()
            return new_found
"""Обработка пользовательских запросов"""
import sys
import view
import model


def start():
    """Запуск программы"""
    while True:
        command = view.user_input(model.get_db())
        input_handler(command)


def exit_program():
    """Завершение работы программы"""
    if view.exit_answer():
        sys.exit()


def show_status_db():
    """Статус базы данных (не открыта//пуста)"""
    if model.state and len(model.get_db()) == 0:
        view.show_message('\nТелефонный справочник пуст!\n')
    elif not model.state and len(model.get_db()) == 0:
        view.show_message('\nТелефонный справочник не открыт!\n')


def input_handler(command: int):
    """Обработка пользовательских запросов"""
    match command:
        case 1:
            model.read_db('database.txt')
            view.show_message('\nТелефонный справочник открыт!\n')
        case 2:
            if model.get_db() and model.state:
                view.show_all_contacts(model.get_db())
            else:
                show_status_db()
        case 3:
            if model.get_db() and model.state:
                found_contact = model.found_contacts(view.find_choice())
                view.show_contact(found_contact)
            else:
                show_status_db()
        case 4:
            if model.state:
                new_contact = view.create_contact(model.get_db())
                model.add_in_contacts(new_contact)
                if view.save_answer():
                    model.save_in_db('database.txt', new_contact)
            else:
                view.show_message('\nТелефонный справочник не открыт!')
        case 5:
            if model.state and model.get_db():
                change = view.change_contact(model.get_db())
                if change is not None:
                    model.change_contact(change)
            else:
                show_status_db()
        case 6:
            if model.state and model.get_db():
                id_contact = view.delete_contact(model.get_db())
                if id_contact is not None:
                    model.delete_in_db(id_contact)
            else:
                show_status_db()
        case 7:
            if model.state and model.get_db():
                if view.save_answer():
                    model.rewrite_db('database.txt', model.get_db())
            else:
                show_status_db()
        case 8:
            exit_program()
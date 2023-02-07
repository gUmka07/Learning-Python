from aiogram import types
import emoji
import text

set_total = 150
total = set_total
game = False
level = 'с глупым ботом'


def update_total():
    """Обновление количества конфет до начального заданного значения
    или по умолчанию"""
    global total
    global set_total
    total = set_total


def set_total_sweets(value: int):
    """Изменение количества конфет"""
    global set_total
    set_total = value
    return set_total


def get_total():
    """Получить текущее количество конфет"""
    global total
    return total


def take_sweets(take: int):
    """Изменение количества конфет после хода игрока или бота"""
    global total
    total -= take
    return total


def new_game():
    """Старт новой игры и обновление настроек"""
    global game
    global total
    if game:
        game = False
    else:
        game = True
        total = set_total
    return game


def check_game():
    """Статус игры"""
    global game
    return game


async def check_win(message: types.Message, player: str, take: int):
    """Проверка возможности выигрыша после хода игрока или бота"""
    name = message.from_user.full_name
    global game
    global level
    if get_total() == 0:
        if player == 'player':
            await message.answer(f'{name} берет {take} {text.declension_sweets(take)[0]}. '
                                 f'\nКонфет больше нет! '
                                 f'\nВыиграл(а) {name}{emoji.emojize("🤓")}'
                                 f'\n\nЕще разок? -> /new_game')
        else:
            await message.answer(f'Конфет больше нет! Выиграл бот!{emoji.emojize("😎")}\n'
                                 'Как насчет реванша?:) -> /new_game')
        new_game()
        return True
    else:
        return False


def change_level():
    """Изменить уровень игры"""
    global level
    if level == 'с глупым ботом':
        level = 'с умным ботом'
    else:
        level = 'с глупым ботом'
    return 
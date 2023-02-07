import emoji

greetings = f', привет!\nДавай сыграем в конфеты{emoji.emojize("🤗")}\n\n' \
            f'Сначала советую посмотреть доступные команды -> /menu'

menu = f', для этой игры используй следующие команды{emoji.emojize("👇")}' \
       f'\n\n1. Старт => /start или /старт\n\n' \
       f'2. Начать игру => /new_game или /игра\n' \
       f'\n3. Правила игры => /rules или /правила\n\n' \
       f'4. Изменить уровень сложности => /level или /уровень\n' \
       f'По умолчанию ты играешь с глупым ботом, попробуй забрать ' \
       f'все конфеты у умного{emoji.emojize("🤯")}\n\n' \
       f'5.Изменить количество конфет => /set_total или /хочу\n(по умолчанию 150 конфет)\n\n' \
       f'6. Все команды => /menu или /меню\n\n' \
       f'7. СТОП-ИГРА => /stop или /стоп'

rules = ', правила в игре простые.\n\nНа столе лежат конфеты. Играют два игрока делая ход друг ' \
        'после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не ' \
        'более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.' \
        '\nПеред началом игры ты можешь поменять уровень и количество конфет.' \
        'Во время игры данные изменения внести не получится.' \
        '\n\nНачать игру => /new_game'

answer1_for_set_total = 'Этой командой можно настроить количество конфет для игры.\n'\
                                      'Введите /set_total или /хочу и количество конфет.'

answer2_for_set_total = 'Kоличество конфет можно изменить только '\
                                  'после окончания игры!'

answer_for_level = 'Изменить уровень можно только после окончания игры!'

stop_game = f'Игра окончена{emoji.emojize("😢")}'


def declension_sweets(take: int):
    """Склонение слова 'конфета' в зависимости от количества"""
    size = len(str(take))
    last_dgt = take % 10
    second_last_dgt = take // 10 % 10
    if (size == 1 and take == 1) or \
            (size > 1 and last_dgt == 1 and second_last_dgt != 1):
        return 'конфету', 'конфета'
    if (size == 1 and take in [2, 3, 4]) or \
            (size > 1 and last_dgt in [2, 3, 4] and second_last_dgt != 1):
        return 'конфеты', 'конфеты'

    return 'конфет', 'конфет'
# def get_index_from_table(field, size: int):
#
#     """
#     Получаем индексы куда можем поставить символ игрока.
#     Спрашиваем у пользователя куда он хочет поставить, проверяем свободна ли ячейка, если занята,
#         то просим заново выбрать куда поставить
#     :param field:
#     :param size:
#     :return: Возвращаем индекс ячейки куда поставил пользователь
#     """
#
#     # TODO Написать реализацию
#
#     return

player_1 = "X"
player_2 = "O"
player_symbols = [player_1, player_2]

def game(player):
    first_player = random.choice(player)
    return first_player

game_over = False
current_player = game(player_symbols)

while game_over == False:
        # 1. Показываем карту
    print_maps()
        # 2. Спросим у играющего куда делать ход
    if player1 == current_player:
        symbol = current_player
        step = int(input("Человек 1, ваш ход: "))
    else:
        symbol =
        step = int(input("Человек 2, ваш ход: "))
    step_maps(step, symbol)  # делаем ход в указанную ячейку
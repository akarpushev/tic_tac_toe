import math
EMPTY_CELL = " "
size = int(input('Введите размер поля: '))

def init_field(size: int, empty_cell: str = EMPTY_CELL):
   return [[empty_cell] * size for _ in range(size)]
#print(init_field(size, EMPTY_CELL))


def draw_field():
   field = init_field(size, EMPTY_CELL)
   for i in range(size):
      print(field[i])
draw_field()

# def get_index_from_table(field, size: int):
#    x = int(input('Введите номер поля: '))
#    index1 = math.ceil(x / size)
#    index2 = x - math.floor(x / size) * size
#    return [index1, index2]
# index_step = get_index_from_table(field, size)
# print(index_step)

# def draw_field(step, symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol

def draw_field_step(x, y, symbol):
    field = init_field(size, EMPTY_CELL)
    field[y - 1][x - 1] = symbol
    #return field
    draw_field()

# def get_win():
#     win = None
#     #return all(x == lst[0] for x in lst)
#
#     for i in range(size):
#         if draw_field_step() == 'X':
#             #print(field[i])
#             #or field[i][1] == "X" and maps[i[2]] == "X":
#             win = 'X'
#         if field[i] == 'O':
#             #and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = 'O'
#     return win


count = 0
player1 = True
game_over = False

#while count < (size * size) or game_over == False:
while game_over == False:
    if player1 == True:
        symbol = 'X'
        print('Ход первого игрока')
        x = int(input('Введите координату х: '))
        y = int(input('Введите координату y: '))
        count += 1
    else:
        symbol = 'O'
        print('Ход второго игрока')
        x = int(input('Введите координату х: '))
        y = int(input('Введите координату y: '))
        count += 1
    draw_field_step(x, y, symbol)
    #field[y - 1][x - 1] = symbol
    #draw_field(field)
#     win = get_win()
#     if win != None:
#         game_over = True
#     else:
#         game_over = False
    player1 = not (player1)
#
# print("Победил", win)




# player1 = 'X'
# player2 = '0'
# current_player = [player1, player2]
# current_player = random.choice(current_player)

# def set_player_in_field(field,
#                         current_player: str,
#                         index_step):
#    """
#       Ставим игрока на поле.
#       По переданным координатам index_step ставим игрока current_player на поле field
#       :param field:
#       :param current_player:
#       :return: Возвращаем поле с текущим ходом игрока
#    """
#    field[index_step[0]][index_step[1]] = current_player
#    return field
# print(set_player_in_field(field, current_player, index_step))


import random

EMPTY_CELL = " "
size = int(input('Введите размер поля: '))

def init_field(size: int, empty_cell: str = EMPTY_CELL):
   return [[empty_cell] * size for _ in range(size)]
#print(init_field(size, EMPTY_CELL))

field = init_field(size, EMPTY_CELL)
def draw_field(field):
   for i in range(size):
      print(field[i])
draw_field(field)

def get_index_from_table(field, size: int):
   """
      Получаем индексы куда можем поставить символ игрока.
      Спрашиваем у пользователя куда он хочет поставить, проверяем свободна ли ячейка, если занята,
          то просим заново выбрать куда поставить
      :param field:
      :param size:
      :return: Возвращаем индекс ячейки куда поставил пользователь
   """
   x = int(input('Введите номер поля: '))
   index1 = (x // size) + 1
   index2 = x - ((x // size)) * size
   return [index1, index2]
#print(get_index_from_table(field, size))
index_step = get_index_from_table(field, size)
#print(index_step)

player1 = 'X'
player2 = '0'
current_player = [player1, player2]
current_player = random.choice(current_player)

def set_player_in_field(field,
                        current_player: str,
                        index_step):
   """
      Ставим игрока на поле.
      По переданным координатам index_step ставим игрока current_player на поле field
      :param field:
      :param current_player:
      :return: Возвращаем поле с текущим ходом игрока
   """
   field[index_step[0]][index_step[1]] = current_player
   return field
print(set_player_in_field(field, current_player, index_step))


def change_player(current_player: str) -> str:
   """
   Определяет кто ходит следующий
   :param current_player: Текущий игрок
   :return:
   """
   current_player != current_player
   return


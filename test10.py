EMPTY_CELL = " "
#size = int(input('Введите размер поля: '))

def init_field(size: int, empty_cell: str = EMPTY_CELL):
   return [[empty_cell] * size for _ in range(size)]
#print(init_field(size, EMPTY_CELL))

field = init_field(size, EMPTY_CELL)
def draw_field(field):
   for i in range(size):
      print(field[i])
draw_field(field)

def game(player: str, size: int) -> Optional[str]:
    """
    Запускает игру
    :param player: игрок которых ходит первым
    :param size: размер поля
    :return: возвращаем None если ничья или возвращаем игрока кто победил
    """

    # Инициализируем поле для игры с заданным размером
    # Отрисовываем текущее поле
    # Инициализируем счетчик ходов
    # Запускаем цикл while с условием пока счетчик меньше числа возможных ходов
    #     Получаем индексы куда поставил игрок (с проверками)
    #     Обновляем поле по тем индексам
    #     Отрисовываем поле
    #     Увеличиваем счётчик ходов
    #     Проводим проверку кто выиграл, если кто-то выиграл то возвращаем кто выиграл
    #     Меняем игрока на следующего
    # Если шаги закончились, а никто не выиграл, значит у нас ничья!



def app():
    """
    Запуск приложения игры крестики-нолики
    :return:
    """
    size = int(input('Введите размер поля: '))
    current_player = input('Введите текущий символ: ')
    return size, current_player

if __name__ == "__main__":
    app()

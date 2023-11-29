EMPTY_CELL = " "
size = int(input('Введите размер поля: '))


def init_field(size: int, empty_cell: str = EMPTY_CELL):
    """
        Создаёт и возвращет пустое поле для игры
        :param size: размер поля
        :param empty_cell: чем заполняется пустая ячейка
        :return: отображение пустого поля в виде листа листов
    """
    return [[empty_cell] * size for _ in range(size)]


print()
field = init_field(size, EMPTY_CELL)


def draw_field(field):
    """
        Функция рисует поле
        :param field: Объект поля
    """
    for i in range(size):
        print(field[i])


draw_field(field)
print()


def field_step(x, y, symbol):
    """
        Функция заполняет клетку символом текущего игрока по переданным координатам
        :param x:
        :param y:
        :param symbol:
        :return field:
        """
    field[y - 1][x - 1] = symbol
    return field


def get_win():
    """
        Функция определяет победителя
            то возвращаем False
        :param field:
        :return win:
    """
    win = None
    for i in range(size):
        if set(field[i]) == set('X'):
            win = "Первый игрок"
        if set(field[i]) == set('0'):
            win = "Второй игрок"
    return win


def game():
    """
        Функция запускает игру
    """
    count = 0
    player1 = True
    while count < size ** 2:
        if player1:
            symbol = 'X'
            print('Ход первого игрока')
            x = int(input('Введите координату х: '))
            y = int(input('Введите координату y: '))
        else:
            symbol = 'O'
            print('Ход второго игрока')
            x = int(input('Введите координату х: '))
            y = int(input('Введите координату y: '))
        count += 1
        field_step(x, y, symbol)
        win = get_win()
        if win is not None:
            draw_field(field)
            print('Победил', win)
            break
        else:
            draw_field(field)
            if count == size ** 2:
                print('Ничья')
        player1 = not player1


if __name__ == "__main__":
    game()

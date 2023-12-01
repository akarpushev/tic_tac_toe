EMPTY_CELL = " "
size = int(input('Введите размер поля: '))
print()


def init_field(size: int, empty_cell: str = EMPTY_CELL):
    """
        Создаёт и возвращет пустое поле для игры
        :param size: размер поля
        :param empty_cell: чем заполняется пустая ячейка
        :return: отображение пустого поля в виде листа листов
    """
    return [[empty_cell] * size for _ in range(size)]


field = init_field(size, EMPTY_CELL)


def draw_field(field):
    """
        Функция рисует поле
        :param field: Объект поля
    """
    for i in range(size):
        print(field[i])


def field_symbol(x, y, symbol):
    """
        Функция заполняет клетку символом текущего игрока по переданным координатам
        :param x:
        :param y:
        :param symbol:
        :return field:
    """
    if field[y-1][x-1] == ' ':
        field[y - 1][x - 1] = symbol
        return True
    else:
        return False


def get_player_move():
    """
        Ввод и проверка координат
        :return x, y:
    """
    while True:
        x = int(input(f'Введите номер столбца от 1 до {size}: '))
        y = int(input(f'Введите номер ряда от 1 до {size}: '))
        if 0 < x <= size and 0 < y <= size:
            return x, y
        else:
            print(f'Неверный ввод. Введите номер от 1 до {size}')


def get_win(field):
    """
        Функция определяет победителя
        :param field:
        :return winner:
    """
    winner = None
    """
        проверка диагоналей 
    """
    diagonal1 = []
    diagonal2 = []
    for i in range(size):
        diagonal1.append(field[i][i])
    if set(diagonal1) == set('X'):
        winner = "Первый игрок"
    if set(diagonal1) == set('0'):
        winner = "Второй игрок"
    for i in range(size-1, -1, -1):
        diagonal2.append(field[i][-i + (size-1)])
    if set(diagonal2) == set('X'):
        winner = "Первый игрок"
    if set(diagonal2) == set('0'):
        winner = "Второй игрок"
    """
        проверка вертикалей 
    """
    column = []
    for i in range(size):
        for j in range(size):
            column.append(field[j][-i + (size-1)])
        for k in range(0, len(column), size):
            if set(column[k: k+size]) == set('X'):
                winner = "Первый игрок"
            if set(column[k: k+size]) == set('0'):
                winner = "Второй игрок"
    """
        проверка горизонталей 
    """
    for i in range(size):
        if set(field[i]) == set('X'):
            winner = "Первый игрок"
        if set(field[i]) == set('0'):
            winner = "Второй игрок"
    return winner


def play_game():
    """
        Функция запускает игру
    """
    current_player = 'первого игрока'
    symbol = 'X'
    while True:
        draw_field(field)
        print()
        print(f'Ход {current_player}')
        x, y = get_player_move()
        if field_symbol(x, y, symbol):
            winner = get_win(field)
            if winner:
                draw_field(field)
                print(f'Победил {winner}')
                break
            elif all(field[i][j] != ' ' for i in range(size) for j in range(size)):
                draw_field(field)
                print('Ничья')
                break
            current_player = 'второго игрока' if current_player == 'первого игрока' else 'первого игрока'
            symbol = '0' if symbol == 'X' else 'X'
        else:
            print(f'Клетка занята. Повторите ход {current_player}.')


if __name__ == "__main__":
    play_game()

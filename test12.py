EMPTY_CELL = " "
size = int(input('Введите размер поля: '))


def init_field(size: int, empty_cell: str = EMPTY_CELL):
   return [[empty_cell] * size for _ in range(size)]


print()
field = init_field(size, EMPTY_CELL)
print()


def draw_field():
   for i in range(size):
      print(field[i])


draw_field()
print()


def field_step(x, y, symbol):
    field[y - 1][x - 1] = symbol
    return field


def draw_field_step():
    #field = field_step(x, y, symbol)
    for i in range(size):
        print(field[i])


def get_win():
    win = None
    for i in range(size):
        if field[i].count('X') == size:
            win = "Первый игрок"
        elif field[i].count('0') == size:
            win = "Второй игрок"
    return win


def game():
    count = 0
    player1 = True
    while count < size ** 2:
        if player1 == True:
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
        print(count)
        win = get_win()
        if win != None:
            draw_field()
            print("Победил", win)
            break
        else:
            draw_field()
            if count == size ** 2:
                print('Ничья')
        player1 = not (player1)


game()

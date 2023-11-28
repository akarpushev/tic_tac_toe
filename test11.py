EMPTY_CELL = " "
size = int(input('Введите размер поля: '))


def init_field(size: int, empty_cell: str = EMPTY_CELL):
   print(f'Размер поля {size} x {size}')
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
        if all(field[i]) == True or all(field[:][i]) == True:
            win = "Первый игрок"
        elif field[i].count('0') == size:
            win = "Второй игрок"
    return win


#game_over = False
count = 0
player1 = True

while count < size ** 2:
    #draw_field()
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
    #print(game_over)
    win = get_win()
    if win != None:
        draw_field()
        print("Победил", win)
        break
        #game_over = True
    else:
        draw_field()
        if count == size ** 2:
            print('Ничья')
        #game_over = False
    player1 = not (player1)

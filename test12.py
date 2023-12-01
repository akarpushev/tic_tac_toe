EMPTY_CELL = " "
size = int(input('Введите размер поля: '))

def init_field(size: int, empty_cell: str = EMPTY_CELL):
    return [[empty_cell] * size for _ in range(size)]

print()
field = init_field(size, EMPTY_CELL)

def draw_field(field):
    for i in range(size):
        print(field[i])

draw_field(field)
print()

def field_symbol(x, y, symbol):
    #while True:
        #try:
        if field[y-1][x-1] == ' ':
            field[y - 1][x - 1] = symbol
            return True
        else:
            print(f'Клетка занята. Повторите ход текущего игрока')
            return False

def get_player_move():
    #while True:
        #try:
        x = int(input(f'Введите координату х от 1 до {size}: '))
        y = int(input(f'Введите координату y от 1 до {size}: '))
        if 0 < x <= size and 0 < y <= size:
            return x, y
        else:
            print(f'Неверный ввод. Введите координату х от 1 до {size}')
            return False

def get_win():
    win = None
    for i in range(size):
        if set(field[i]) == set('X'):
            win = "Первый игрок"
        if set(field[i]) == set('0'):
            win = "Второй игрок"
    return win

def game():
    #count = 0
    player1 = True
    while True:
        if player1:
            print('Ход первого игрока')
            symbol = 'X'
            x, y = get_player_move()
            if field_symbol(x, y, symbol):
                draw_field(field)
                win = get_win()
                if win is not None:
                    draw_field(field)
                    print('Победил', win)
                    break
                elif all(field[i][j] != ' ' for i in range(size) for j in range(size)):
                    draw_field(field)
                    print('Ничья')
                    break

        else:
            print('Ход второго игрока')
            symbol = 'O'
            x, y = get_player_move()
            if field_symbol(x, y, symbol):
                draw_field(field)
                win = get_win()
                if win is not None:
                    draw_field(field)
                    print('Победил', win)
                    break
                elif all(field[i][j] != ' ' for i in range(size) for j in range(size)):
                    draw_field(field)
                    print('Ничья')
                    break

        #count += 1
        #field_symbol(x, y, symbol)
        #draw_field(field)
        #win = get_win()
        #if win is not None:
            #draw_field(field)
            #print('Победил', win)
            #break
        #elif all(field[i][j] != ' ' for i in range(size) for j in range(size)):
            #draw_field(field)
            #print('Ничья')

        player1 = not player1


if __name__ == "__main__":
    game()

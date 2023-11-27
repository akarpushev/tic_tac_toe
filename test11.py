EMPTY_CELL = " "
size = int(input('Введите размер поля: '))

def init_field(size: int, empty_cell: str = EMPTY_CELL):
   field = [[empty_cell] * size for _ in range(size)]
   return field

def draw_field():
   field = init_field(size, EMPTY_CELL)
   for i in range(size):
      print(field[i])
draw_field()

def field_step(x, y, symbol):
    field = init_field(size, EMPTY_CELL)
    field[y - 1][x - 1] = symbol
    return field
    #draw_field_step()

def draw_field_step():
    field = field_step(x, y, symbol)
    for i in range(size):
        print(field[i])
#draw_field_step()

count = 0
player1 = True
game_over = False

while count < (size * size): #or game_over == False:
#while game_over == False:
    if player1 == True:
        symbol = 'X'
        print('Ход первого игрока')
        x = int(input('Введите координату х: '))
        y = int(input('Введите координату y: '))
        #count += 1
    else:
        symbol = 'O'
        print('Ход второго игрока')
        x = int(input('Введите координату х: '))
        y = int(input('Введите координату y: '))
        #count += 1
    count += 1
    field_step(x, y, symbol)
    draw_field_step()
    print(count)
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





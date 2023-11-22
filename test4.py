size = int(input('Введите размер поля: '))
map = list(range(1, (size**2)+1))
print(map)
def print_map():
    for i in range(size):
        for j in range(size):
            print(map[i], end=" ")

print_map()

#step = int(input('Введите номер поля: '))

def step_map(step, symbol):
    index = map.index(step)
    map[index] = symbol

#step_map(step, 'X')
#print(map)
#
#
game_over = False
player1 = True
#
while game_over == False:
    print_map()
    if player1 == True:
        symbol = "X"
        step = int(input("Игрок 1, введите номер поля: "))
    else:
        symbol = "O"
        step = int(input("Игрок 2, введите номер поля: "))
    step_map(step, symbol)  # делаем ход в указанную ячейку
#     win = get_result()  # определим победителя
#     if win != "":
#         game_over = True
#     else:
#         game_over = False
#
    player1 = not (player1)


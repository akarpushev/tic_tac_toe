import random
EMPTY_CELL = " "

def init_field(size: int, empty_cell: str = EMPTY_CELL) -> list[list]:
    return [[empty_cell] * size for i in range(size)]

size = int(input('Введите размер: '))
#print(init_field(size, EMPTY_CELL))
field = init_field(size, EMPTY_CELL)

def draw_field(field):
    for i in field:
        print(i)

draw_field(field)

map = list(range(1, (size**2)+1))
player_1 = "X"
player_2 = "O"
player_symbols = [player_1, player_2]
def step():
    current_symbol = random.choice(player_symbols)
    step = int(input('Введите ход: '))
    map[step-1] = current_symbol
    print(map)

step()

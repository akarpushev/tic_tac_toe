import random

EMPTY_CELL = " "

def init_field(size: int, empty_cell: str = EMPTY_CELL) -> list[list]:
    return [[empty_cell] * size for i in range(size)]

size = int(input('Введите число: '))
#print(init_field(size, EMPTY_CELL))
field = init_field(size, EMPTY_CELL)

def draw_field(field):
    for i in field:
        print(i)

draw_field(field)


player_1 = "X"
player_2 = "O"
player_symbols = [player_1, player_2]

def game(player):
    first_player = random.choice(player)
    return first_player

#print(game(player_symbols))

def step_field(step, player):

    ind = maps.index(step)
    maps[ind] = symbol





a = [
    ['X', 'X', 'X'],
    ['X', ' ', ' '],
    ['X', ' ', ' ']
]
size = 3
def get_win():
    win = None
    for i in range(size):
        if all(a[i]) == 'X': # or all(a[:][i]) == 'X':
        #if a[:][0] == 'X':
        #if a[0].count('X') == size:
            win = "Первый игрок"
        elif a[i].count('0') == size:
            win = "Второй игрок"
    print(win)

get_win()



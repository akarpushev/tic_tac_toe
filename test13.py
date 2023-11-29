a = [
    ['X', 'X', 'P'],
    ['X', ' ', ' '],
    ['X', '0', ' ']
]
size = 3
def get_win():
    win = None
    for i in range(size):
        for j in range(size):
            if set(a[i]) == set('X') or set(a[::][j]) == set('X'):
                win = "Первый игрок"
            elif set(a[i]) == set('0') or set(a[i][0]) == set('0'):
                win = "Второй игрок"
    print(win)

get_win()




size = int(input('Введите размер поля: '))
board = list(range(1, size+1))
print(board)
map = list(range(1, (size**2)+1))
print(map)

s = 0
def draw_board(board):
    for i in range(size):
        for j in range(size):
            print(board[i][j])

        #print((("|", map[i]) * size), "|")

        #print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        #print("-" * 13)
draw_board(board)

# S = 0
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         S += A[i][j]
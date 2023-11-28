size = int(input('Введите размер поля: '))
# row = [1]
# map = [row]
# for i in range(2, size+1):
#     row.append(i)
# for i in range(size-1):
#     map.append(map[i])
# print(map)
map = list(range(1, (size**2)+1))
print(map)

def draw_field():
   for i in range(size):
       for j in range(size):
           print(map[i], end='\n')


draw_field()



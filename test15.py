maps = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = []
for i in range(3):

    for j in range(3):
        a.append(maps[j][-i+2])
    print(a[i:i+3])



print(a)
print(a[:3])
print(a[3:6])





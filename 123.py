n = int(input())

array = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        array[j][i] = i*n +j

for data in array:
    print(data)

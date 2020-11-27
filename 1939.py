n, m = map(int,input().split())

array = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    array[a][b] = c
    array[b][a] = c
for i in range(1,n+1):
    print(array[i][1:])
f1, f2 = map(int,input().split())
temp = 0
if array[f1][f2] != 0:
    temp = array[f1][f2]

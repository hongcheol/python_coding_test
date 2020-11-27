import sys
sys.setrecursionlimit(100000)


def dfs(x,y,count):
    visited[x][y] = True
    count += 1
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if array[nx][ny] and not visited[nx][ny]:
            count = dfs(nx,ny,count)
    return count
n = int(input())
array = [[0]*n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
for i in range(n):
    string = input()
    for j in range(n):
        array[i][j] = int(string[j])
    result = 0
ans = list()
for i in range(n):
    for j in range(n):
        if array[i][j] and not visited[i][j]:
            ans.append(dfs(i,j,0))
            result += 1
ans.sort()
print(result)
for i in range(result):
    print(ans[i])

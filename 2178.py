from collections import deque


n,m = map(int,input().split())
maze = [[] for _ in range(n)]

for i in range(n):
    s = input()
    for char in s:
        maze[i].append(int(char))

print(bfs(maze))

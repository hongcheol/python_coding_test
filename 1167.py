import sys
from collections import deque
V = int(sys.stdin.readline())
tree = [[] for _ in range(V+1)]
r = 0
'''
def dfs(graph,visited, start_node,l):
    global r,V
    if r<l:
        r = l
    visited[start_node] = True
    for data in graph[start_node]:
        if visited[data[0]]:
            continue
        else:
            l += data[1]
            dfs(graph, visited, data[0],l)
            l -= data[1]
            visited[data[0]] = False
'''
def bfs(graph,visited,start_node):
    visited[start_node] = True
    queue = deque()
    queue.append([0, start_node])
    max_dist, vertex = 0, 0

    while queue:
        cur_dist, cur_vertex = queue.popleft()

        if cur_dist > max_dist:
            max_dist = cur_dist
            vertex = cur_vertex

        for node in graph[cur_vertex]:
            if not visited[node[0]]:
                queue.append((cur_dist+node[1], node[0]))
                visited[node[0]] = True
    return max_dist, vertex

for _ in range(V):
    input_data = list(map(int, sys.stdin.readline().split()))
    node_num = input_data[0]
    for i in range(1, len(input_data)-2,2):
        temp_tuple = (input_data[i],input_data[i+1])
        tree[node_num].append(temp_tuple)


visited = [False] * (V + 1)
r,end1 = bfs(tree, visited, 1)
for i in range(1,V+1):
    visited[i] = False
answer,end2 = bfs(tree, visited, end1)
print(answer)
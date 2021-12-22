from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 1
position = (1, 1)

def bfs(graph, x, y):
    queue = deque([x, y])
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        return False
    while position != (n, m):
        
        return result


for i in range(n):
    for j in range(m):
        if bfs(n, m) == True:
            print(result)



print(result)
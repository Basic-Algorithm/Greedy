import numpy as np

n, m = list(map(int, input().split()))

# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

visited = [False] * np.ones(shape = (n, m), dtype = np.int8)
# result = 0
# for i in graph:
#     for j in graph[i]:
#         if graph[i][j] == 0:
#             visited[i][j] = True


print(visited)
# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
from itertools import combinations, product


def sol(x, y, n):
    color = graph[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):

            if color != graph[i][j]:
                sol(x, y, n // 2)
                sol(x + n // 2, y, n // 2)
                sol(x, y + n // 2, n // 2)
                sol(x + n // 2, y + n // 2, n // 2)
                return
    res[color] += 1


n = int(input())
graph = []
res = [0, 0]
for _ in range(n):
    graph.append(list(map(int, input().split())))

sol(0, 0, n)
print(res[0])
print(res[1])
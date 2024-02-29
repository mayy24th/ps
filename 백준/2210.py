# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
from itertools import combinations, product
import sys

input = sys.stdin.readline

def dfs(x, y, num):
    if len(num) == 6:
        if num not in res:
            res.append(num)
        return
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx<0 or ny<0 or nx>=5 or ny>=5:
            continue
        dfs(nx, ny, num + graph[nx][ny])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
graph = []
res = []
for _ in range(5):
    graph.append(list(input().split()))

for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])

print(len(res))
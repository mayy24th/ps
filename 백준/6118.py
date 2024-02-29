# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
from itertools import combinations, product
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
dist = [0 for _ in range(n+1)]
visit = [False for _ in range(n+1)]

def bfs(start):
    q = deque()
    q.append(start)
    visit[start] = True
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if visit[next]: continue

            dist[next] = dist[cur] + 1
            q.append(next)
            visit[next] = True

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(1)
print(dist.index(max(dist)), max(dist), dist.count(max(dist)))
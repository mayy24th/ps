# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
from itertools import combinations, product
import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visit = [False for _ in range(n+1)]
parent = [0 for _ in range(n+1)]
q = deque()
q.append(1)

while q:
    v = q.popleft()
    visit[v] = True

    for n in graph[v]:
        if visit[n]: continue
        q.append(n)
        parent[n] = v

print(* parent[2:])
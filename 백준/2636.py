# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

def isZero():
    res = 0
    for i in graph:
        res += sum(i)

    if res == 0: return 0
    else: return res

def bfs(i, j):
    global one
    visit[i][j] = True

    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx<0 or ny<0 or nx>=N or ny>=M or visit[nx][ny]: continue

            if graph[nx][ny] == 0:
                q.append((nx, ny))
                visit[nx][ny] = True
            if graph[nx][ny] == 1:
                one.append((nx, ny))
                visit[nx][ny] = True

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

time = 0
ans = []

while True:
    if isZero() == 0:
        break
    else: ans.append(isZero())

    one = deque()
    visit = [[False for _ in range(M)] for _ in range(N)]
    bfs(0, 0)

    while one:
        x, y = one.popleft()
        graph[x][y] = 0
    time += 1
print(time)
print(ans[-1])
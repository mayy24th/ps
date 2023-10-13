# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

def isZero(graph):
    ans = 0
    for g in graph:
        ans += sum(g)

    if ans == 0: return True
    else: return False

def bfs(i, j):
    global coordinate

    q = deque()
    q.append((i, j))
    visit[i][j] = True

    while q:
        x, y = q.popleft()
        c = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx<0 or ny<0 or nx>=N or ny>=M or visit[nx][ny]: continue

            if graph[nx][ny] == 0:
                c += 1
            else:
                q.append((nx, ny))
                visit[nx][ny] = True

        coordinate.append((x, y, c))
    return 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

flag = 0
cnt = 0
year = 0
while True:
    # for v in graph:
    #     print(*v)
    cnt = 0
    coordinate = deque()
    visit = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and not visit[i][j]:
                cnt += bfs(i, j)
                flag = 1
    while coordinate:
        x, y, c = coordinate.popleft()
        graph[x][y] -= c
        if graph[x][y] < 0: graph[x][y] = 0

    if cnt >= 2:
        break

    if isZero(graph) and cnt == 0:
        year = 0
        break
    year += 1
print(year)
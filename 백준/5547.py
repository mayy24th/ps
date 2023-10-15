# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
import sys, heapq

input = sys.stdin.readline

dx = [-1, -1, 0, 0, 1, 1]
dy = [[0, 1, -1, 1, 0, 1], [-1, 0, -1, 1, -1, 0]] #홀, 짝


def bfs(i, j):
    visit[i][j] = True
    q = deque()
    q.append((i, j))
    cnt = 0
    while q:
        x, y = q.popleft()

        for i in range(6):
            nx = x + dx[i]

            if x % 2 == 1:
                ny = y + dy[0][i]
            else:
                ny = y + dy[1][i]

            if nx < 0 or ny < 0 or nx >= N+2 or ny >= M+2 or visit[nx][ny]: continue

            if graph[nx][ny] == 1:
                cnt += 1
            elif graph[nx][ny] == 0:
                q.append((nx, ny))
                visit[nx][ny] = True
    return cnt


M, N = map(int, input().split())

graph = [[0 for _ in range(M + 2)]]
for _ in range(N):
    tmp = list(map(int, input().split()))
    graph.append([0] + tmp + [0])
graph.append([0 for _ in range(M + 2)])

visit = [[False for _ in range(M + 2)] for _ in range(N + 2)]

print(bfs(0, 0))


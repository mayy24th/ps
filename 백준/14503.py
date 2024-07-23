# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
from itertools import combinations, product

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(sx, sy, sd):
    ans = 0
    q = deque()
    q.append((sx, sy))
    d = sd

    while (q):
        x, y = q.popleft()

        if graph[x][y] == 0 and not isClean[x][y]:
            isClean[x][y] = True
            ans += 1

        flag = 0
        for i in range(3, -1, -1):
            nx, ny = x + dx[(d + i) % 4], y + dy[(d + i) % 4]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue

            if graph[nx][ny] == 0 and not isClean[nx][ny]:
                q.append((nx, ny))
                d = (d + i) % 4
                flag = 1
                break

        if flag == 0:
            nx, ny = x - dx[d], y - dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue

            if graph[nx][ny] == 0 or graph[nx][ny] == 2:
                q.append((nx, ny))

    return ans


n, m = map(int, input().split())
start_x, start_y, start_d = map(int, input().split())
graph = []
isClean = [[False for _ in range(m)] for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))

print(bfs(start_x, start_y, start_d))

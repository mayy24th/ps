from collections import deque
import sys

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
M, N, H = map(int, input().split())

# 그래프 입력
graph = [[] for _ in range(H)]
for i in range(H):
    for _ in range(N):
        graph[i].append(list(map(int, input().split())))
max = -1
q = deque()


def bfs():
    global max

    while q:
        z, x, y = q.popleft()

        # 최대값 저장
        if max < graph[z][x][y]: max = graph[z][x][y]

        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]

            if nz < 0 or nz >= H or nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if graph[nz][nx][ny] == -1 or graph[nz][nx][ny] > 0: continue

            graph[nz][nx][ny] = graph[z][x][y] + 1
            q.append((nz, nx, ny))


for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                q.append((i, j, k))

bfs()

for i in range(H):
    for j in range(N):
        if 0 in graph[i][j]:
            print(-1)
            exit()
print(max - 1)
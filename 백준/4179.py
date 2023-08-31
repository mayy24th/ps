from collections import deque
import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

R, C = map(int, input().split())

# 지훈이와 불의 이동 거리
j_dist = [[-1 for _ in range(C)] for _ in range(R)]
f_dist = [[-1 for _ in range(C)] for _ in range(R)]

graph = []
for _ in range(R):
    graph.append(input().rstrip())

# 지훈이와 불의 큐
j_q = deque()
f_q = deque()
for i in range(R):
    for j in range(C):
        # 지훈이와 불의 시작 위치를 각자의 큐에 담고 이동거리를 0으로 바꿈
        if graph[i][j] == 'J':
            j_q.append((i, j))
            j_dist[i][j] = 0
        if graph[i][j] == 'F':
            f_q.append((i, j))
            f_dist[i][j] = 0

while f_q:
    x, y = f_q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if nx<0 or ny<0 or nx>=R or ny>=C: continue


        # 벽 or 이미 불이 지나간 경우 continue
        if graph[nx][ny] == '#' or f_dist[nx][ny] != -1: continue

        f_dist[nx][ny] = f_dist[x][y]+1 # 새로운 좌표에 현재거리+1 저장
        f_q.append((nx, ny))    # 새로운 좌표 삽입

while j_q:
    x, y = j_q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        # 범위를 벗어남 => 탈출
        if nx<0 or ny<0 or nx>=R or ny>=C:
            print(j_dist[x][y]+1)
            exit(0)

        # continue
        # 1. 이동하려는 위치에 벽 or 이미 지나간 자리
        if graph[nx][ny] == '#' or j_dist[nx][ny] != -1: continue
        # 2. 이동하려는 위치에 불 and 불 이동시간이 지훈이의 현재 이동시간+1보다 짧은 경우(이미 불)
        if f_dist[nx][ny] <= j_dist[x][y]+1 and f_dist[nx][ny] != -1: continue

        j_dist[nx][ny] = j_dist[x][y]+1 # 이전 거리+1 저장
        j_q.append((nx, ny))    # 새로운 좌표 삽입

print("IMPOSSIBLE")
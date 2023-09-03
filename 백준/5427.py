from collections import deque
import sys
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

tc = int(input())
def sg_bfs():
    while sg_q:
        x, y = sg_q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 탈출 조건
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                print(sg_dist[x][y]+1)
                return
            if graph[nx][ny] == '#' or sg_dist[nx][ny] != -1: continue
            if fire_dist[nx][ny] != -1 and sg_dist[x][y]+1 >= fire_dist[nx][ny]: continue

            sg_dist[nx][ny] = sg_dist[x][y]+1
            sg_q.append((nx, ny))
    print("IMPOSSIBLE")

for _ in range(tc):
    m, n = map(int, input().split())
    graph = []

    fire_q = deque()
    sg_q = deque()
    for _ in range(n):
        graph.append(list(input().rstrip()))

    # 불과 상근이의 이동 거리 초기화
    fire_dist = [[-1 for _ in range(m)] for _ in range(n)]
    sg_dist = [[-1 for _ in range(m)] for _ in range(n)]

    # 불과 상근이의 시작 위치 각 큐에 push
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '*':
                fire_q.append((i, j))
                fire_dist[i][j] = 0
            if graph[i][j] == '@':
                sg_q.append((i, j))
                sg_dist[i][j] = 0

    # 불 bfs
    while fire_q:
        x, y = fire_q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m: continue
            if graph[nx][ny] == '#' or fire_dist[nx][ny] != -1: continue

            fire_dist[nx][ny] = fire_dist[x][y]+1
            fire_q.append((nx, ny))

    # 상근 bfs
    sg_bfs()
from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1, 0, 0]
dy = [1, 0, -1, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    cnt = 0
    while q:
        z, x, y = q.popleft()
        if graph[z][x][y] == 'E':
            print("Escaped in {} minute(s).".format(visit[z][x][y]))
            return

        for i in range(6):
            nz, nx, ny = z+dz[i], x+dx[i], y+dy[i]

            if nz<0 or nz>=L or nx<0 or nx>=R or ny<0 or ny>=C: continue
            if graph[nz][nx][ny] == '#' or visit[nz][nx][ny] != -1: continue

            visit[nz][nx][ny] = visit[z][x][y]+1
            q.append((nz, nx, ny))

    print("Trapped!")

while True:
    L, R, C = map(int, input().split())

    # 종료 조건
    if (L, R, C) == (0, 0, 0): break

    q = deque()
    graph = []
    visit = [[[-1 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    idx = 0
    for i in range(L):
        graph.append([list(input().rstrip()) for _ in range(R)])
        tmp = input()
        for j in range(R):
            for k in range(C):
                if graph[i][j][k] == "S":
                    q.append((i, j, k))
                    visit[i][j][k] = 0
    bfs()
import copy
from collections import deque
import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
graph = []
for _ in range(n): graph.append(list(map(int, input().rstrip())))

# visit[x][y][0] : 벽을 뚫지 않고 지나온 거리
# visit[x][y][1] : 벽을 뚫고 지나온 거리
visit = [[[0, 0] for _ in range(m)] for _ in range(n)]
visit[0][0][0] = 1

def bfs():
    q = deque()
    q.append((0, 0, 0))
    while q:
        x, y, w = q.popleft()

        if (x, y) == (n-1, m-1):
            return visit[x][y][w]

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m: continue

            # 방문하지 않은 다음 위치에 대하여
            if visit[nx][ny][w] == 0:

                # 1. 벽이 아닌 경우
                if graph[nx][ny] == 0:
                    q.append((nx, ny, w))
                    visit[nx][ny][w] = visit[x][y][w]+1

                # 2. 벽이면서 현재 위치가 벽이 아닌 경우
                if graph[nx][ny] == 1 and w == 0:
                    q.append((nx, ny, 1))
                    visit[nx][ny][1] = visit[x][y][w]+1

    return -1

print(bfs())
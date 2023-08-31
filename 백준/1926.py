from collections import deque
import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(i, j):
    cnt = 0
    q = deque()
    q.append((i, j))
    visit[i][j] = 1
    cnt += 1

    while q:
        x, y = q.pop()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue

            if graph[nx][ny] == 1 and visit[nx][ny] == 0:
                q.append((nx, ny))
                visit[nx][ny] = 1
                cnt += 1

    return cnt


n, m = map(int, input().split())
graph = []
visit = [[0 for _ in range(m)] for _ in range(n)]
chk, ans = 0, 0
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if visit[i][j] == 0 and graph[i][j] == 1:
            chk += 1
            ans = max(ans, bfs(i, j))

print(chk)
print(ans)
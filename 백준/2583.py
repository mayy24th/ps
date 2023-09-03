from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visit[i][j] = 1

    ans = 0
    while q:
        x, y = q.pop()
        ans = max(ans, visit[x][y])
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n: continue
            if graph[nx][ny] == 1: continue
            if visit[nx][ny] == 0:
                q.append((nx, ny))
                visit[nx][ny] = 1
                ans += 1

    return ans

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

m, n, k = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(m)]
visit = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

ans = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and visit[i][j] == 0:
            ans.append(bfs(i, j))

print(len(ans))
ans.sort()
print(*ans)

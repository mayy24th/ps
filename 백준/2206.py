import copy
from collections import deque
import sys
input = sys.stdin.readline

def find_fir_block():
    global ans
    q = deque()
    q.append((1, 0, 0))   # (거리, x, y)
    visit[0][0] = 1
    while q:
        d, x, y = q.pop()

        # 벽없이 끝까지 도달 가능 가능한 경우
        if (x, y) == (n-1, m-1):
            ans = d
            return

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m: continue

            # 처음 만나는 벽
            if graph[nx][ny] == '1' and visit[nx][ny] == 0:
                fir_block.append((d+1, nx, ny))
                visit[nx][ny] = 1
            # 이동 경로
            if graph[nx][ny] == '0' and visit[nx][ny] == 0:
                q.append((d+1, nx, ny))
                visit[nx][ny] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
graph = []
visit = [[0 for _ in range(m)] for _ in range(n)]

fir_block = deque()
for _ in range(n):
    graph.append(list(input().rstrip()))

ans = 10e9

# 벽 찾기
find_fir_block()
print()
while fir_block:
    gg = copy.deepcopy(graph)
    vv = [[0 for _ in range(m)] for _ in range(n)]
    vv[0][0] = 1
    a, b, c = fir_block.popleft()

    gg[b][c] = '0'
    q = deque()
    q.append((1, 0, 0))

    while q:
        d, x, y = q.popleft()
        # 벽없이 끝까지 도달 가능 가능한 경우
        if (x, y) == (n-1, m-1):
            ans = min(d, ans)
            break

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m: continue
            if gg[nx][ny] == '1': continue

            if gg[nx][ny] == '0' and vv[nx][ny] == 0:
                q.append((d+1, nx, ny))
                vv[nx][ny] = 1

if ans == 10e9: print(-1)
else : print(ans)

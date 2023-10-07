# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline
def bfs(i, j, color):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = 1

    # c는 터지는 경우 원소들을 .으로 바꾸기 위해 좌표 저장하는 큐
    c = deque()
    c.append((i, j))

    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx<0 or ny<0 or nx>11 or ny>5: continue

            if graph[nx][ny] == color and (nx, ny) not in c:
                c.append((nx, ny))
                q.append((nx, ny))
                cnt += 1
    if cnt < 4: return 0
    else:
        while c:
            x, y = c.popleft()
            graph[x][y] = '.'
        return 1
def refresh(graph):
    for j in range(6):
        tmp = []
        for i in range(12):
            if graph[i][j] != '.':
                tmp.append(graph[i][j])
        tmp = ['.' for _ in range(12-len(tmp))] + tmp

        for i in range(11, -1, -1):
            graph[i][j] = tmp[i]
graph = []
ans = 0
for _ in range(12):
    graph.append(list(input().rstrip()))

# 종료조건 bfs 결과를 누적해서 더했는데 값이 0이면 종료
while True:
    cnt = 0
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.':
                v = bfs(i, j, graph[i][j])
                if v == 1:
                    cnt += 1

    if cnt == 0: break
    else :
        ans += 1
        refresh(graph)

print(ans)
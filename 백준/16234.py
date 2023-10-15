# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def printGraph(graph):
    print("graph")
    for i in graph:
        print(*i)
    print("@@@@@@@@@@@")

def bfs(i, j):
    res = deque()
    q = deque()
    res.append((i, j))
    q.append((i, j))

    cnt = 1
    sum = graph[i][j]

    visit[i][j] = True
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=N or visit[nx][ny]: continue

            gap = abs(graph[x][y]-graph[nx][ny])
            if L <= gap <= R:
                q.append((nx, ny))
                res.append((nx, ny))
                visit[nx][ny] = True
                cnt += 1
                sum += graph[nx][ny]

    if cnt != 1:
        for x, y in res:
            graph[x][y] = sum//cnt  # 인구수 조정
    return cnt

N, L, R = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


ans = 0
tmp = 1
while True:
    flag = 0
    visit = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visit[i][j]: tmp = bfs(i, j)
            if tmp != 1:    # 한번이라도 이동이 있으면
                flag = 1

    # 종료 조건 : 한번도 인구 조정이 일어나지 않았을 경우
    if flag == 0:
        break
    else: ans += 1
print(ans)
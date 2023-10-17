# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from itertools import permutations
from collections import deque
import sys, heapq

input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def dfs(x, y, value, depth):
    global ans
    if depth == 4:
        ans = max(ans, value)
        return
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M and not visit[nx][ny]:
            visit[nx][ny] = True
            dfs(nx, ny, value+graph[nx][ny], depth+1)
            visit[nx][ny] = False

N, M = map(int, input().split())
visit = [[False for _ in range(M)] for _ in range(N)]
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

ans = 0
for i in range(N):
    for j in range(M):
        # ㅗ ㅓ ㅏ ㅜ 모양을 제외한 나머지
        visit[i][j] = True
        dfs(i, j, graph[i][j], 1)
        visit[i][j] = False

        # ㅗ ㅓ ㅏ ㅜ
        for x in range(4):
            value = graph[i][j]
            for y in range(3):
                # (x+y)%4 => 012, 123, 230, 301
                nx, ny = i+dx[(x+y)%4], j+dy[(x+y)%4]
                if nx<0 or ny<0 or nx>=N or ny>=M:
                    value = 0
                    break
                value += graph[nx][ny]
            ans = max(value, ans)

print(ans)
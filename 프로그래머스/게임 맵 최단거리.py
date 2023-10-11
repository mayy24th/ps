# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    q = deque()
    q.append((0, 0))

    visit = [[False for _ in range(m)] for _ in range(n)]
    visit[0][0] = True

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    maps[0][0] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m or maps[nx][ny]==0: continue

            if visit[nx][ny]:
                if maps[nx][ny] > maps[x][y]+1:
                    maps[nx][ny] = maps[x][y]+1
                continue

            q.append((nx, ny))
            maps[nx][ny] = maps[x][y]+1
            visit[nx][ny] = True

    ans = maps[n-1][m-1]

    if ans == 1: return -1
    else: return ans

maps = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,0],
        [0,0,0,0,1]]
solution(maps)
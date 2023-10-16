# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
from itertools import combinations
import sys, heapq
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(comb):
    price = 0

    for x, y in comb:
        visit[x][y] = True
        price += graph[x][y]

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if visit[nx][ny]: return -1 # 겹치는 경우

            price += graph[nx][ny]
            visit[nx][ny] = True
    return price

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 전체 좌표 쌍 저장
coordinate = [(x, y) for x in range(1, N-1) for y in range(1, N-1)]

ans = 10e9
for comb in combinations(coordinate, 3):
    visit = [[False for _ in range(N)] for _ in range(N)]
    tmp = bfs(comb)
    if tmp == -1: continue

    ans = min(ans, tmp)

print(ans)

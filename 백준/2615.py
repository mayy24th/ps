# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
from itertools import combinations
import sys, heapq
input = sys.stdin.readline

# \ / ㅣ ㅡ
dx = [0, -1, -1, -1, 0, 0, 1, 1, 1]
dy = [0, -1, 1, 0, -1, 1, 0, -1, 1]

def bfs(i, j, color, d):
    # color : 1(black) / 2(white)
    global ans
    cnt = 1
    q = deque()
    q.append((i, j))
    ans = (i, j)
    visit[i][j] = True

    while q:
        x, y = q.popleft()

        x1, y1 = x + dx[d], y + dy[d]
        x2, y2 = x + dx[-d], y + dy[-d]

        if 0 <= x1 <= 18 and 0 <= y1 <= 18 and graph[x1][y1] == color and not visit[x1][y1]:
            q.append((x1, y1))
            visit[x1][y1]= True
            cnt += 1
            if ans[1] > y1:
                ans = (x1, y1)
            elif ans[1] == y1 and ans[0] > x1:
                ans = (x1, y1)
        if 0 <= x2 <= 18 and 0 <= y2 <= 18 and graph[x2][y2] == color and not visit[x2][y2]:
            q.append((x2, y2))
            visit[x2][y2] = True
            cnt += 1
            if ans[1] > y2:
                ans = (x2, y2)
            elif ans[1] == y2 and ans[0] > x2:
                ans = (x2, y2)

    return cnt
ans = (-1, -1)
graph = []
for _ in range(19):
    graph.append(list(map(int, input().split())))
cnt = -1
for i in range(19):

    for j in range(19):
        if graph[i][j] in (1, 2):
            for d in range(1, 5):
                x1, y1 = i+dx[d], j+dy[d]
                x2, y2 = i+dx[-d], j+dy[-d]
                if 0<=x1<=18 and 0<=x2<=18 and 0<=y1<=18 and 0<=y2<=18 and graph[i][j] in (graph[x1][y1], graph[x2][y2]):
                    visit = [[False for _ in range(19)] for _ in range(19)]
                    cnt = bfs(i, j, graph[i][j], d)

                    if cnt == 5:
                        print(graph[i][j])
                        print(ans[0]+1, ans[1]+1)
                        exit()

print(0)
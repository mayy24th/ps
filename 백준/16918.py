# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

R, C, N = map(int, input().split())
graph = []

for _ in range(R):
    graph.append(list(input().rstrip()))

q = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

allBomb = [['O' for _ in range(C)] for _ in range(R)]
allDot = [['.' for _ in range(C)] for _ in range(R)]
def printGraph(graph):
    # print("{}초 후 그래프".format(sec))
    for i in range(R):
        for j in range(C):
            # 출력 형식 틀려서 계속틀림..
            print(graph[i][j], end='')
        print()

sec = 1
while True:
    if sec == N: break
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'O':
                q.append((i, j))

    graph = copy.deepcopy(allBomb)
    sec += 1
    if sec == N: break
    if not q:
        graph = copy.deepcopy(allDot)
    while q:
        x, y = q.popleft()
        graph[x][y] = '.'
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx<0 or ny<0 or nx>=R or ny>=C: continue

            graph[nx][ny] = '.'

    sec += 1

printGraph(graph)
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
    global sword
    q = deque()
    q.append((i, j))
    visit[i][j] = True

    # print("CHK")
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx<0 or ny<0 or nx>=N or ny>=M: continue
            if graph[nx][ny]==-1 or visit[nx][ny]: continue

            q.append((nx, ny))
            graph[nx][ny] = graph[x][y]+1
            visit[nx][ny] = True

N, M, T = map(int, input().split())
visit = [[False for _ in range(M)] for _ in range(N)]
sword = (-1, -1)
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            graph[i][j] = -1
        if graph[i][j] == 2:
            sword = (i, j)
            graph[i][j] = -2

bfs(0, 0)
x, y = sword[0], sword[1]
N -= 1
M -= 1
res = graph[N][M]

if graph[N][M] != 0 and (x, y) != (-1, -1):
    res = min(graph[N][M], graph[x][y]+(N-x)+(M-y))
elif graph[N][M] == 0 and (x, y) != (-1, -1):
    res = graph[x][y]+(N-x)+(M-y)
if (graph[N][M] == 0 and graph[x][y] == -2) or res > T: print("Fail")
else: print(res)

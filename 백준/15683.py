import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

# # print graph
# def printGraph(arr):
#     print("---------------")
#     for v in arr:
#         print(*v)
#     print("---------------")

# 사각지대 갯수
def zeroCount(arr):
    count = 0
    for i in range(len(arr)):
        count += arr[i].count(0)
    return count
# 감시
def watch(arr, dir, x, y):
    for i in dir:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]

            if nx<0 or ny<0 or nx>=N or ny>=M or graph[nx][ny] == 6: break

            if arr[nx][ny] == 0:
                arr[nx][ny] = -1    # 감시 상태로 변경

# dfs
def dfs(arr, depth):
    global ans
    if depth == len(cctv):
        count = zeroCount(arr)
        # printGraph(arr)
        # print(count)
        ans = min(count, ans)
        return

    arr_copy = copy.deepcopy(arr)
    num, x, y = cctv[depth]

    for dir in direction[num]:
        watch(arr_copy, dir, x, y)
        dfs(arr_copy, depth+1)
        arr_copy = copy.deepcopy(arr)

#    0
#  2   3
#    1
#    북, 남, 서, 동
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
cctv = []
graph = []
direction = [
    [],
    # 1: 북, 남, 서, 동
    [[0], [1], [2], [3]],
    # 2: (북남), (서동)
    [[0, 1], [2, 3]],
    # 3: (북동), (동남), (남서), (북서)
    [[0, 3], [3, 1], [1, 2], [2, 0]],
    # 4: (북동서), (북동남), (남동서), (북남서)
    [[0, 2, 3], [0, 3, 1], [1, 3, 2], [0, 1, 2]],
    # 5: 동서남북
    [[0, 1, 2, 3]]
]

ans = 10e9
for _ in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(len(graph[-1])):
        if graph[-1][j] in [1, 2, 3, 4, 5]:
            cctv.append([graph[-1][j], len(graph)-1, j])

dfs(graph, 0)
print(ans)
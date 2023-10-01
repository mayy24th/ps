import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

# 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 해당 칸에서 인접한 칸 중 좋아하는 학생이 있는 칸의 수
def likeCnt(student, i, j):
    res = 0
    for k in range(4):
        if 0 <= i+dx[k] and i+dx[k] < N and 0 <=j+dy[k] and j+dy[k] < N:
            if seat[i + dx[k]][j + dy[k]] in like[student]:
                res += 1
        else:
            continue
    return res

# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 해당 칸에서 인접한 칸 중 비어있는 칸의 수
def emptyCnt(student, i, j):
    res = 0
    for k in range(4):
        if 0 <= i+dx[k] and i+dx[k] < N and 0 <=j+dy[k] and j+dy[k] < N:
            if seat[i + dx[k]][j + dy[k]] == 0:
                res += 1
        else: continue
    return res


dx = [1, 0, -1, 0]
dy = [0, 1, 0,-1]

N = int(input())
like = dict()
seat = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N*N):
    tmp = list(map(int, input().split()))
    like[tmp[0]] = tmp[1:]
    likemax = -1
    emptymax = -1
    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if seat[i][j] == 0:
                liketmp = likeCnt(tmp[0], i, j)
                emptytmp = emptyCnt(tmp[0], i, j)
                if likemax < liketmp:
                    likemax = liketmp
                    emptymax = emptytmp
                    x, y = i, j
                elif likemax == liketmp and emptymax < emptytmp:
                    likemax = liketmp
                    emptymax = emptytmp
                    x, y = i, j
    seat[x][y] = tmp[0]

score = [0, 1, 10, 100, 1000]
res = 0
for i in range(N):
    for j in range(N):
        res += score[likeCnt(seat[i][j], i, j)]

print(res)
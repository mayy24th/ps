# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from itertools import permutations
from collections import deque
import sys, heapq

input = sys.stdin.readline

def makeGraph(i, j):
    brown, yellow = 0, 0
    for x in range(i):
        for y in range(j):
            if x in (0, i-1) or y in (0, j-1): brown += 1
            else: yellow += 1
    return [brown, yellow]

def solution(brown, yellow):
    total = brown + yellow
    for i in range(3, (total//3)+1):
        for j in range(3, i+1):
            if i*j == total:
                cnt = makeGraph(j, i)
                if cnt[0] == brown and cnt[1] == yellow: return [i, j]

print(solution(24, 24))
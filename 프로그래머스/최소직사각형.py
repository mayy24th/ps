# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
import sys, heapq

input = sys.stdin.readline

def solution(sizes):
    for i in range(len(sizes)):
        sizes[i].sort()

    mx = sizes[0][0]
    my = sizes[0][1]

    for i in range(1, len(sizes)):
        mx = max(mx, sizes[i][0])
        my = max(my, sizes[i][1])
    answer = mx*my
    return answer

print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
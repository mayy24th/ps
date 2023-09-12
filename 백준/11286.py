import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    num = int(input())

    if num == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(num), num))
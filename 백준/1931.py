import copy
from collections import deque
import sys, heapq

input = sys.stdin.readline

n = int(input())
time = []
for _ in range(n):
    time.append(list(map(int, input().split())))

# 배열이름.sort(key=lambda x:x[0])
time.sort(key=lambda x:x[0])
time.sort(key=lambda x:x[1])

ans = 1
cur = time[0]
for i in range(1, n):
    if cur[1] <= time[i][0]:
        cur = time[i]
        ans += 1
print(ans)


import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())
box = []
for _ in range(M):
    box.append(list(map(int, input().split())))
box.sort(key=lambda x: x[1])

ans = 0
arr = [C for _ in range(N+1)]

for s, r, cnt in box:
    cnt = min(cnt, min(arr[s:r]))
    if cnt != 0:
        for i in range(s, r):
            arr[i] -= cnt
        ans += cnt

print(ans)
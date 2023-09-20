import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

# 11000이랑 같은 풀이방법
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort()
q = []
heapq.heappush(q, arr[0][1])

for i in range(1, n):
    if q[0] <= arr[i][0]:
        heapq.heappop(q)
        heapq.heappush(q, arr[i][1])
    else:
        heapq.heappush(q, arr[i][1])

print(len(q))
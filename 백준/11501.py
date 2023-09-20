import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    ans = 0
    n = int(input())
    arr = list(map(int, input().split()))

    mx = -1
    for i in range(len(arr)-1, -1, -1):
        if mx >= arr[i]:
            ans += (mx-arr[i])
        else:
            mx = arr[i]
    print(ans)

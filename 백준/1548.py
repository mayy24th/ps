# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from itertools import permutations
from collections import deque
import sys, heapq

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
arr.sort()
ans = 2
if N <= 2:
    print(N)
else:
    for i in range(N-2):
        for j in range(i+2, N):
            if arr[i]+arr[i+1] > arr[j]:
                ans = max(ans, j-i+1)
            else : break
    print(ans)
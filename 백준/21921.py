# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
from itertools import combinations, product
import sys

input = sys.stdin.readline

# 슬라이딩 윈도우
N, X = map(int, input().split())
arr = list(map(int, input().split()))
if max(arr) == 0:
    print("SAD")
    exit(0)

cur = sum(arr[0:X])
res, cnt = sum(arr[0:X]), 1

for i in range(X, N):
    cur += arr[i]
    cur -= arr[i - X]

    if cur > res:
        res = cur
        cnt = 1
    elif cur == res:
        cnt += 1

print(res)
print(cnt)


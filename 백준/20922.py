# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
from itertools import combinations, product
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = [0 for _ in range(100_001)]
left, right = 0, 0
res = 0

while right < N:
    if cnt[arr[right]] < K:
        cnt[arr[right]] += 1
        right += 1
    else:
        # K보다 작아질때 까지 왼쪽 값을 계속 이동
        cnt[arr[left]] -= 1
        left += 1
    res = max(res, right - left)

print(res)

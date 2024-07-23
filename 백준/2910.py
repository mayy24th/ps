# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
from itertools import combinations, product

n, c = map(int, input().split())
nums = list(map(int ,input().split()))
cnt = {}

for num in nums:
    if num not in cnt:
        cnt[num] = 1
    else:
        cnt[num] += 1

cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)

for res in cnt:
    for _ in range(res[1]):
        print(res[0], end=' ')
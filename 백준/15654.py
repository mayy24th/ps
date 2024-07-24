# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
from itertools import combinations, product

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
res = []

def sol(depth):
    if depth == m:
        print(*res)
        return

    for i in range(n):
        if num[i] in res:
            continue
        res.append(num[i])
        sol(depth + 1)
        res.pop()

sol(0)
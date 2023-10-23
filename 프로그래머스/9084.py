# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from itertools import permutations
from collections import deque
import sys, heapq

input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    money = int(input())
    dp = [1] + [0 for _ in range(money)]
    for v in arr:
        for i in range(v, money+1):
            if i < v: continue
            dp[i] += dp[i-v]

    # print(dp)
    print(dp[money])
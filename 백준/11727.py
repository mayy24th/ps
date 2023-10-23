# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from itertools import permutations
from collections import deque
import sys, heapq

input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(1001)] # 2xi를 채우는 방법의 수
# dp = 0, 1, 3, 5, 11 ...
dp[0], dp[1], dp[2], dp[3], dp[4] = 0, 1, 3, 5, 11
for i in range(5, n+1):
    dp[i] = dp[i-2]*2 + dp[i-1]

print(dp[n] % 10007)

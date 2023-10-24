# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from itertools import permutations
from collections import deque
import sys, heapq

input = sys.stdin.readline

# C 이후부터의 최소값을 찾는 문제
C, N = map(int, input().split())
dp = [10e9 for _ in range(C+100)]
dp[0] = 0
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: x[1])

for cost, customer in arr:
    for i in range(customer, C+100):
        dp[i] = min(dp[i-customer]+cost, dp[i])

print(min(dp[C:]))
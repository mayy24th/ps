# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
from itertools import combinations, product
import sys

input = sys.stdin.readline


def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if (i, j) == (0, 0): continue
            if [j+1, i+1] in puddles:
                dp[i][j] = 0
            else:
                if i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

    ans = dp[n-1][m-1] % 1000000007
    return ans


print(solution(4, 3, [ [2,3]]))

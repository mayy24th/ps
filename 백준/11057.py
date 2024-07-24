# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
from itertools import combinations, product

n = int(input())

# 0으로 시작 가능
# 길이가 2이고 3로 끝나는 오르막수 : 03, 13, 23, 33
# 길이가 3이고 1로 끝나는 오르막수 : 001, 011, 111
# 길이가 3이고 2로 끝나는 오르막수 : 002, 012, 022, 112, 122, 222
# 뒷자리수 0  1  2  3  4  5  6  7  8  9
# 길이 1: 1  1  1  1  1  1  1  1  1  1
# 길이 2: 1  2  3  4  5  6  7  8  9  10
# 길이 3: 1  3  6  10 15 21 28 36 45 55
# 길이 4: 1  4  10 20 35 56 84 120 165 220
# => (i,j) = (i-1,j) + (i,j-1)

dp = [1 for _ in range(10)]
for i in range(1, n):
    for j in range(1, 10):
        dp[j] += dp[j - 1]

print(sum(dp) % 10007)
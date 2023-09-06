import copy
from collections import deque
import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 9)

x = int(input())

dp = [0] * 1000001
ans = [0] * 1000001
for i in range(2, x+1):
    dp[i] = dp[i-1] + 1
    ans[i] = i-1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i//3]+1
        ans[i] = i//3
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        ans[i] = i//2

print(dp[x])
tmp = x
while tmp>=1:
    print(tmp, end=' ')
    tmp = ans[tmp]
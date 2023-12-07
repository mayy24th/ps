import sys

input = sys.stdin.readline


def solution(n):
    dp = [0, 1, 1] + [0 for _ in range(n + 1)]
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n] % 1234567
import sys

input = sys.stdin.readline

def solution(triangle):
    dp = [[0 for _ in range(i+1)] for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    dp[1][0] = dp[0][0] + triangle[1][0]
    dp[1][1] = dp[0][0] + triangle[1][1]

    for i in range(2, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:  # 왼쪽 끝
                dp[i][j] = dp[i-1][j]+triangle[i][j]
            elif j == len(triangle[i])-1:   # 오른쪽 끝
                dp[i][j] = dp[i-1][-1]+triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

    answer = max(dp[-1])
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(triangle)
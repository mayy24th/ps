# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
import sys, heapq

input = sys.stdin.readline

def solution(numbers, target):
    answer = 0

    def dfs(depth, res):
        nonlocal answer
        if depth == len(numbers):
            if res == target:
                answer += 1
            return

        dfs(depth+1, res+numbers[depth])
        dfs(depth+1, res-numbers[depth])
    dfs(0, 0)
    return answer


numbers = [4, 1, 2, 1]
target = 4

print(solution(numbers, target))
# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

def solution(n, computers):
    visit = [False for _ in range(n)]
    answer = 0

    for i in range(n):
        if visit[i]: continue

        q = deque()
        q.append(i)
        visit[i] = True
        while q:
            cur = q.popleft()

            for j in range(n):
                if not visit[j] and computers[cur][j] == 1:
                    q.append(j)
                    visit[j] = True

        answer += 1
    return answer

computers =[[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(3, computers))

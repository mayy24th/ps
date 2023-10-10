import copy
from collections import deque
import sys, heapq

input = sys.stdin.readline


# 파이썬 제출 -> 시간초과
# pypy3 제출 -> 정답
def bfs(start):
    cnt = 0
    q = deque([start])
    visit = [False for _ in range(N + 1)]
    visit[start] = True

    while q:
        cur = q.popleft()
        cnt += 1  # 방문

        for n in graph[cur]:
            if not visit[n]:
                visit[n] = True
                q.append(n)
    return cnt


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    # a가 b를 신뢰한다. => b를 해킹하면 a도 해킹할 수 있다.
    a, b = map(int, input().split())
    graph[b].append(a)

ans = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    ans[i] = bfs(i)

for i in range(1, N + 1):
    if ans[i] == max(ans):
        print(i, end=' ')

# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
from itertools import combinations, product

def bfs():
    q = deque()
    q.append((x_home, y_home))

    while q:
        x_new, y_new = q.popleft()

        if (abs(x_fest - x_new) + abs(y_fest - y_new)) <= 1000:
            print("happy")
            return

        for i in range(n):
            if not visit[i] and (abs(conv[i][0] - x_new) + abs(conv[i][1] - y_new)) <= 1000:
                visit[i] = True
                q.append(conv[i])

    print("sad")
    return

t = int(input())

# 한번에 갈 수 있는 최대 거리는 맥주 20개 * 50미터 = 1000미터
for _ in range(t):
    n = int(input())  # 편의점 갯수
    conv = []
    visit = [False for _ in range(n)]

    x_home, y_home = map(int, input().split())

    for i in range(n):
        conv.append(list(map(int, input().split())))
    x_fest, y_fest = map(int, input().split())

    bfs()


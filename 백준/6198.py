import copy
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()
ans = 0

for _ in range(n):

    # 입력된 높이보다 왼쪽에 있는 더 높은 빌딩이 나올 때 까지 pop
    h = int(input())
    while q and q[-1] <= h: q.pop()

    # len(q) : 입력된 높이의 빌딩을 내려다보고 있는 빌딩의 수
    ans += len(q)
    q.append(h)

print(ans)
from collections import deque
import sys

N, L = map(int, input().split())
arr = list(map(int, input().split()))

D = deque([])
for i in range(N):
    # 큐에 (idx(0), data(1)) 삽입
    if D and D[0][0] <= i - L:  # 이전 최소값이 구간을 벗어난 경우 pop
        D.popleft()

    while D and arr[i] < D[-1][1]:
        D.pop()  # 새로 들어온 값이 기존 값보다 작으면 기존 값 pop

    D.append((i, arr[i]))

    print(D[0][1], end=' ')
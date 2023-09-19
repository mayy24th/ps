import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

# 1931처럼 인덱스 둘 다 정렬해서 일반 큐로 하다가 안풀려서 참고
# https://hongcoding.tistory.com/79
n = int(input())
time = []
for _ in range(n): time.append(list(map(int, input().split())))

time.sort()
hq = []
heapq.heappush(hq, time[0][1])

for i in range(1, n):
    if hq[0] <= time[i][0]:
        heapq.heappop(hq)
        heapq.heappush(hq, time[i][1])
    else:
        heapq.heappush(hq, time[i][1])

print(len(hq))
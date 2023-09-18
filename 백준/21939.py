import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

N = int(input())
mx_heap = []
mn_heap = []
sol = {}

for _ in range(N):
    P, L = map(int, input().split())
    heapq.heappush(mx_heap, (-L, -P))
    heapq.heappush(mn_heap, (L, P))
    sol[P] = True

M = int(input())
for _ in range(M):
    op = input().split()

    if op[0] == 'recommend':
        x = int(op[1])
        if x == 1:
            while not sol[-mx_heap[0][1]]: heapq.heappop(mx_heap)
            print(-mx_heap[0][1])
        else :
            while not sol[mn_heap[0][1]]: heapq.heappop(mn_heap)
            print(mn_heap[0][1])
    elif op[0] == 'add':
        P, L = int(op[1]), int(op[2])
        while not sol[-mx_heap[0][1]]: heapq.heappop(mx_heap)
        while not sol[mn_heap[0][1]]: heapq.heappop(mn_heap)

        sol[P] = True
        heapq.heappush(mx_heap, (-L, -P))
        heapq.heappush(mn_heap, (L, P))
    else : # solved
        P = int(op[1])
        sol[P] = False


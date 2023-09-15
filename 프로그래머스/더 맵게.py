import copy
from collections import deque
import sys, heapq

input = sys.stdin.readline

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if scoville[0] >= K:
            return answer
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        else:
            fir = heapq.heappop(scoville)
            sec = heapq.heappop(scoville)

            new = fir + (sec*2)
            heapq.heappush(scoville, new)
            answer += 1

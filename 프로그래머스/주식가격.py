import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

def solution(prices):
    answer = [0  for _ in range(len(prices))]

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1

            if prices[i] > prices[j]:
                break

    return answer

print(solution([1,2,3,2,3]))
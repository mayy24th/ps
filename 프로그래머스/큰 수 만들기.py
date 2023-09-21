import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

# 콤비네이션 실패
def solution(number, k):
    answer = deque()
    for n in number:
        # 큐가 비어있지 않고
        # 큐의 마지막 원소보다 들어온 숫자가 더 크고
        # 삭제해야 할 갯수가 아직 남아있다면
        while answer and answer[-1] < n and k > 0:
            answer.pop()
            k -= 1
        answer.append(n)

    answer = list(answer)
    if k > 0:
        answer = answer[:-k]

    return ''.join(answer)
# 987654321, 3

print(solution("987654321", 3))
# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
import sys, heapq

input = sys.stdin.readline

# 참고 : https://lottegiantsv3.tistory.com/27
def solution(tickets):
    tickets.sort(key=lambda x: (x[0], x[1]))
    answer = []

    q = deque() # (현재 공항, 이동 경로, 사용한 티켓의 인덱스)
    q.append(("ICN", ["ICN"], []))

    while q:
        airport, path, used = q.popleft()

        if len(used) == len(tickets):
            answer = path
            break

        for idx, ticket in enumerate(tickets):
            if ticket[0] == airport and not idx in used:
                q.append((ticket[1], path + [ticket[1]], used + [idx]))
    return answer


# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

print(solution(tickets))
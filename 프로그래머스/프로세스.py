import copy
from collections import deque
import sys, heapq

input = sys.stdin.readline


def solution(priorities, location):
    answer = 0

    # 11~14 : (인덱스, 요소) 쌍으로 큐에 넣음
    q = [[i] for i in range(len(priorities))]
    for i in range(len(priorities)):
        q[i].append(priorities[i])
    q = deque(q)

    while True:
        tmp = q.popleft()

        if any(tmp[1] < elem[1] for elem in q):
            # 큐에서 뽑아낸 원소보다 큰 원소가 큐에 있으면 다시 append
            q.append(tmp)
        else:
            # 뽑아낸 원소보다 큰 원소가 없으면 ans+=1
            answer += 1

            # 만약 실행된 원소의 처음 위치가 location과 같다면 리턴
            if tmp[0] == location:
                return answer


print(solution([2, 1, 3, 2], 2))
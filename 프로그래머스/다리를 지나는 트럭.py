import copy
from collections import deque
import sys, heapq

input = sys.stdin.readline


# 트럭이 다리에 들어가고 나서부터의 시간 체크를 어떻게 해야될지 몰라서 검색
# 참고
# https://jie0025.tistory.com/428
# https://latte-is-horse.tistory.com/130
def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 다리 위 트럭의 총 무게
    sum_weight = 0

    # 다리 위 트럭의 움직임을 나타내는 큐
    bridge = deque([0 for _ in range(bridge_length)])

    # 아직 다리에 올라가지 않은 대기 트력
    wait = deque(truck_weights)

    while wait:
        cross = bridge.popleft()  # 건넘
        sum_weight -= cross  # 무게 뺌

        if sum_weight + wait[0] <= weight and len(wait) > 0:
            new = wait.popleft()
            sum_weight += new
            bridge.append(new)
        else:
            bridge.append(0)

        answer += 1

    # 마지막 트럭이 들어가고 반복문 종료
    # -> 마지막 트럭이 지나가는 시간(다리거리)를 더해줌
    answer += bridge_length
    return answer

print(solution(2, 10, [7, 4, 5, 6]))

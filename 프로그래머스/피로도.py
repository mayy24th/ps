# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from itertools import permutations
from collections import deque
import sys, heapq

input = sys.stdin.readline

def solution(k, dungeons):
    answer = 0
    idx = [i for i in range(0, len(dungeons))]
    pers = permutations(idx, len(dungeons))
    for per in pers:
        tmp = 0
        cur = k
        for p in per:
            if dungeons[p][0] <= cur:
                cur -= dungeons[p][1]
                tmp += 1
        answer = max(tmp, answer)
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))
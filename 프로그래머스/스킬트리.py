# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

def solution(skill, skill_trees):
    answer = 0

    for st in skill_trees:
        idx = 0
        cnt = 0
        for sk in st:
            if not sk in skill:
                cnt += 1
                continue

            if sk == skill[idx] and idx < len(skill):
                cnt += 1
                idx += 1
        if cnt == len(st): answer += 1

    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))
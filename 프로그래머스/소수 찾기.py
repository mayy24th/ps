# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from itertools import permutations
from collections import deque
import sys, heapq

input = sys.stdin.readline

def solution(numbers):
    answer = 0
    prime = []
    for i in range(1, len(numbers)+1):
        combis = permutations(numbers, i)
        for comb in combis:
            num = ''
            flag = 1
            for c in comb:
                num += c
            if int(num) in (0, 1): continue
            #for k in range(2, int(num)): -> 시간 초과
            for k in range(2, int(int(num) ** 0.5) + 1):
                if int(num)%k == 0: flag = 0

            if flag == 1 and int(num) not in prime:
                prime.append(int(num))
    return len(prime)

print(solution("17"))
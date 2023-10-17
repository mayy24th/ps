# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from itertools import product
from collections import deque
import sys, heapq

input = sys.stdin.readline

def solution(word):
    arr = ['A', 'E', 'I', 'O', 'U']
    case = []
    for i in range(1, 6):
        tmp = list(product(arr, repeat = i))
        for c in tmp:
            case.append(''.join(c))

    case.sort()
    return case.index(word)+1

print(solution('AAAAE'))

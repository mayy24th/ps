# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

coordinate = {1: (0, 0), 2: (0, 1), 3: (0, 2),
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2),
              '*': (3, 0), 0: (3, 1), '#': (3, 2)}

def solution(numbers, hand):
    answer = ''

    cur_left, cur_right = '*', '#'

    for number in numbers:
        # left
        if number in (1, 4, 7):
            cur_left = number
            answer += 'L'
        # right
        elif number in (3, 6, 9):
            cur_right = number
            answer += 'R'
        else:
            # 거리 = abs(현재위치x-이동할위치x) + abs(현재위치y-이동할위치y)
            dist_left = abs(coordinate[cur_left][0] - coordinate[number][0]) + abs(coordinate[cur_left][1] - coordinate[number][1])
            dist_right = abs(coordinate[cur_right][0] - coordinate[number][0]) + abs(coordinate[cur_right][1] - coordinate[number][1])

            if dist_left == dist_right:
                if hand == 'right': answer += 'R'
                else: answer += 'L'
            else:
                if dist_left > dist_right: answer += 'R'
                else : answer += 'L'

            if answer[-1] == 'R' : cur_right = number
            else : cur_left = number
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

print(solution(numbers, hand))
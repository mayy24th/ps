import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

# boj 19598 처럼 힙을 이용해 풀다가 틀림
# 투포인터로 다시 품
def solution(people, limit):
    ans = 0
    people.sort()
    left, right = 0, len(people)-1
    while left <= right:
        if people[left] + people[right] <= limit:
            ans += 1
            left += 1
            right -= 1
        else:
            ans += 1
            right -= 1

    return ans

# 40 50 60 60 150 160
# 200
arr = list(map(int, input().split()))
l = int(input())
print(solution(arr, l))

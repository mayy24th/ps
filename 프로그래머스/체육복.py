import copy
from collections import deque
import sys, heapq
input = sys.stdin.readline

def solution(n, lost, reserve):
    answer = n

    # 삭제된 원소 뒤의 값들이 앞으로 밀리면서 삭제가 안되는 원소가 생김 -> set으로 해결
    # for i in reserve:
    #     if i in lost:
    #         reserve.remove(i)
    #         lost.remove(i)

    ll = set(lost) - set(reserve)
    rr = set(reserve) - set(lost)

    for i in rr:
        if i-1 in ll:
            ll.remove(i-1)
        elif i+1 in ll:
            ll.remove(i+1)

    return answer - len(ll)

n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))

print(solution(n, lost, reserve))
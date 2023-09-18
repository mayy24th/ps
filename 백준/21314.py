import copy
from collections import deque
import sys, heapq

input = sys.stdin.readline

mk = input().rstrip()

max = ""
min = ""

cnt = 0
# 최대가 되는 경우 : K가 나올때까지 M의 갯수를 세어주고 K가 나오면 숫자로 바꿈, M->1
# 최소가 되는 경우 : M으로 시작해서 M으로 끝나는 구간을 숫자로 바꿈, K->5

for i in range(len(mk)):
    if mk[i] == 'M':
        cnt += 1
        if i == len(mk)-1: # 마지막 인덱스
            max += ('1' * cnt)
            min += str(10**(cnt-1))

    else : # K
        if cnt == 0:
            max += '5'
            min += '5'
        else :
            max += str(10**cnt * 5)
            min += (str(10**(cnt-1))+'5')
        cnt = 0

print(max)
print(min)
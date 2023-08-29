from collections import deque
import sys

tc = int(input())
for _ in range(tc):
    p = input()         # 함수
    n = int(input())    # 배열 갯수

    arr = input()       # 배열
    q = deque(arr[1:-1].split(','))

    if n == 0 :
        q = []

    rev = 0
    for pp in p:
        if pp == 'R': rev += 1   # 함수 R
        else :                   # 함수 D
            if len(q) == 0:
                print("error")
                break
            elif rev % 2 == 0: q.popleft()
            elif rev % 2 == 1: q.pop()

    else:
        if rev % 2 == 1:
            q.reverse()
        #','.join(q) => q의 원소들을 "1,2,3,4,5" 형태로 바꿔줌
        print('[' + ','.join(q) + ']')

import copy
from collections import deque
import sys, heapq

input = sys.stdin.readline

def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)-1):
        # if phone_book[i] in phone_book[i+1]: -> 테스트케이스 하나 통과 못함 이유 모르겠음..
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True
from collections import deque
import sys

ans = 0
arr = input()
q = deque()
q.append(arr[0])

for i in range(1, len(arr)):
    if arr[i] == ')':
        if arr[i-1] == '(': # 닫는 경우 이전 인덱스가 여는 괄호일 경우 => 레이저
            q.pop()
            ans += len(q)
        else:
            q.pop()
            ans += 1
    else:
        q.append(arr[i])
print(ans)


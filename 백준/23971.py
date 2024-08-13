# 배열이름.sort(key=lambda x: (x[0], x[1]))

import copy, math
from collections import deque
from itertools import combinations, product

h, w, n, m = map(int, input().split())

a = math.ceil(w/(m+1))
b = math.ceil(h/(n+1))
# ceil : 반올림
# ceil.(길이/(간격+1)) = 최대로 들어갈 수 있는 수
print(a*b)
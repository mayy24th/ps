from collections import defaultdict
from bisect import bisect_left
from itertools import combinations

def solution(info, query):
    answer = []

    dict = defaultdict(list)

    for i in info:
        i = i.split()
        condition = i[:-1]
        score = int(i[-1])

        for n in range(5):
            for combi in combinations([0, 1, 2, 3], n):
                tmp = condition[:]
                for idx in combi:
                    tmp[idx] = '-'
                key = ' '.join(tmp)
                dict[key].append(score)

    for key in dict:
        dict[key].sort()

    for q in query:
        q = q.replace(" and ", " ").split()
        key = ' '.join(q[:-1])
        score = int(q[-1])

        if key in dict:
            scores = dict[key]
            idx = bisect_left(scores, score)
            answer.append(len(scores) - idx)
        else:
            answer.append(0)

    return answer

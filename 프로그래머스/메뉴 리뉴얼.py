from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []

    for c in course:
        menus = []
        for order in orders:
            menus += combinations(sorted(order), c)

        counter = Counter(menus)

        if len(counter) > 0 and max(counter.values()) > 1:
            for menu in counter:
                if counter[menu] == max(counter.values()):
                    answer.append("".join(menu))

    return sorted(answer)
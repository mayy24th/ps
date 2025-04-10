def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero = 0
    for lotto in lottos:
        if lotto in win_nums:
            cnt = cnt + 1
        elif lotto == 0:
            zero = zero + 1

    rank = [6, 6, 5, 4, 3, 2, 1]
    answer.append(rank[cnt+zero])
    answer.append(rank[cnt])
    return answer
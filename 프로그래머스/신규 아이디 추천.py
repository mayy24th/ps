def solution(new_id):
    answer = ''

    # 1
    new_id = new_id.lower()

    # 2
    for c in new_id:
        if 'a' <= c <= 'z' or '0' <= c <= '9' or c in "-_.":
            answer += c

    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    print(answer)

    # 4
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]

    # 5
    if len(answer) == 0: answer = 'a'

    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7
    if len(answer) <= 2:
        answer = answer + (answer[-1] * (3 - len(answer)))

    return answer
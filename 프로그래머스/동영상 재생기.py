def solution(video_len, pos, op_start, op_end, commands):
    answer = ''

    video_len = int(video_len.split(":")[0]) * 60 + int(video_len.split(":")[1])
    pos = int(pos.split(":")[0]) * 60 + int(pos.split(":")[1])
    op_start = int(op_start.split(":")[0]) * 60 + int(op_start.split(":")[1])
    op_end = int(op_end.split(":")[0]) * 60 + int(op_end.split(":")[1])
    if op_start <= pos <= op_end: pos = op_end

    for cmd in commands:
        if cmd == "prev":
            if pos >= 10:
                pos = pos - 10
            else:
                pos = 0
        elif cmd == "next":
            if pos + 10 > video_len:
                pos = video_len
            else:
                pos = pos + 10

        if op_start <= pos <= op_end: pos = op_end

    answer = str(pos // 60).zfill(2) + ":" + str(pos % 60).zfill(2)

    return answer
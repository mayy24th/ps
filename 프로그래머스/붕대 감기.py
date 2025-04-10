def solution(bandage, health, attacks):
    end_time = attacks[-1][0]
    max_health = health
    count = 0
    for i in range(end_time + 1):
        if attacks[0][0] == i:
            health = health - attacks.pop(0)[1]
            count = 0
            if health <= 0: return -1
        else:
            count = count + 1
            health = health + bandage[1]
            if count == bandage[0]:
                health = health + bandage[2]
                count = 0;

            if health >= max_health: health = max_health

    return health
def solution(players, callings):
    rank = {name: i for i, name in enumerate(players)}
    for call in callings:
        idx = rank[call]

        players[idx], players[idx - 1] = players[idx - 1], players[idx]

        rank[players[idx]] = idx
        rank[players[idx - 1]] = idx - 1

    return players
ranks = {"diamond": 1, "iron": 2, "stone": 3}
results = []

def backtrack(picksd, minerals, exh):
    if sum(picksd.values()) == 0 or not minerals:
        results.append(exh)
        return

    for key in picksd.keys():
        if picksd[key] > 0:
            new_picksd = picksd.copy()
            new_picksd[key] -= 1

            next_minerals = minerals[:5]
            new_exh = 0

            for mineral in next_minerals:
                if ranks[key] <= ranks[mineral]:
                    new_exh += 1
                else:
                    new_exh += 5 ** (ranks[key] - ranks[mineral])

            backtrack(new_picksd, minerals[5:], exh + new_exh)

def solution(picks, minerals):

    picksd = {"diamond": picks[0], "iron": picks[1], "stone": picks[2]}
    backtrack(picksd, minerals, 0)

    return min(results)

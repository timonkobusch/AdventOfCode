

def p1(lines):
    times = [int(x) for x in (lines[0].split()[1:])]
    distances = [int(x) for x in (lines[1].split()[1:])]
    ans = 1
    for time, distance in zip(times, distances):
        margin = 0
        for speed in range(1, time):
            distance_race = speed * (time - speed)
            if distance_race > distance:
                margin += 1
        ans *= margin

    return ans


def p2(lines):
    time = int(lines[0].split()[1])
    distance = int(lines[1].split()[1])
    l = 0
    r = time
    while l+1 < r:
        middle = (l+r) // 2
        race_distance = middle * (time - middle)
        if race_distance > distance:
            r = middle
        else:
            l = middle

    return time - (r*2) + 1
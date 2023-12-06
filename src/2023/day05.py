def map_seeds(mapping, seeds):
    mapping = dict(sorted(mapping.items(), key=lambda x: x[0]))
    for i in range(len(seeds)):
        for key, (length, dest) in mapping.items():
            if key <= seeds[i] < key + length:
                seeds[i] = seeds[i] + (dest - key)
                break
    return seeds


def p1(lines):
    seeds = lines[0].split(':')[1].strip().split()
    seeds = list(map(lambda x: int(x), seeds))
    lines[0] = ''
    mapping = {}

    for line in lines:
        if line == '':
            continue
        elif 'map' in line:
            seeds = map_seeds(mapping, seeds)
            mapping.clear()
        else:
            (dest, start, length) = map(lambda x: int(x), list(line.split()))
            mapping[start] = (length, dest)

    seeds = map_seeds(mapping, seeds)
    seeds = sorted(seeds)


    return seeds[0]


def map_seeds_p2(mapping, seeds):

    mapping = dict(sorted(mapping.items(), key=lambda x: x[0]))
    new_seeds = []
    while len(seeds) > 0:
        (seed_start, seed_end) = seeds.pop()
        in_intervall = False
        for source_start, (length, dest) in mapping.items():
            source_end = source_start + length - 1
            offset = dest - source_start
            # not in intervall
            if seed_end < source_start or seed_start > source_end:
                continue
            elif seed_start < source_start:
                in_intervall = True
                if seed_end <= source_end:
                    seeds.append([seed_start, source_start - 1])
                    new_seeds.append([source_start + offset, seed_end + offset])
                else:
                    seeds.append([seed_start, source_start - 1])
                    new_seeds.append([source_start + offset, source_end + offset])
                    seeds.append([source_end + 1, seed_end])
            elif seed_start >= source_start:
                in_intervall = True
                if seed_end <= source_end:
                    new_seeds.append([seed_start + offset, seed_end + offset])
                else:
                    new_seeds.append([seed_start + offset, source_end + offset])
                    seeds.append([source_end+1, seed_end])
        if not in_intervall:
            new_seeds.append([seed_start, seed_end])


    return new_seeds


def p2(lines):
    raw = lines[0].split(':')[1].strip().split()
    seeds = []
    for i in range(len(raw)):
        if i % 2 == 1:
            seeds.insert(0, [int(raw[i-1]), int(raw[i]) + int(raw[i-1])])
    lines[0] = ''
    mapping = {}


    for line in lines:
        if line == '':
            continue
        elif 'map' in line:
            seeds = map_seeds_p2(mapping, seeds)
            mapping.clear()
        else:
            (dest, start, length) = map(lambda x: int(x), list(line.split()))
            mapping[start] = (length, dest)

    seeds = map_seeds_p2(mapping, seeds)
    min_seed = seeds[0][0]
    for seed in seeds:
        min_seed = min(min_seed, seed[0])

    return min_seed

import re


def p1(f):
    ans = 0
    for l, line in enumerate(f):

        for match in re.finditer('\d+', line):
            (start, end) = match.span()
            add = False
            for y in range(max(0, l - 1), min(len(f), l + 2)):
                for x in range(max(0, start - 1), min(len(f[0]), end + 1)):
                    if f[y][x] != '.' and not f[y][x].isnumeric():
                        add = True
            if add:
                ans += int(match.group())
    return ans


def p2(f):
    gears = {}
    for l, line in enumerate(f):
        for match in re.finditer('\d+', line):
            number = int(match.group())

            (start, end) = match.span()

            for y in range(max(0, l - 1), min(len(f), l + 2)):
                for x in range(max(0, start - 1), min(len(f[0]), end + 1)):
                    if f[y][x] == '*':
                        if (y, x) in gears:
                            gears[(y, x)] += [number]
                        else:
                            gears[(y, x)] = [number]
    return sum([value[0] * value[1] for value in gears.values() if len(value) == 2])

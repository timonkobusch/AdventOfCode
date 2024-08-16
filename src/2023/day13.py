# python main.py --sample true --year 2023 13
def checkVerticalMirror(pattern):
    line_length = len(pattern[0])
    possible_mirrors = list(zip(range(line_length - 1), range(1, line_length)))
    for line in pattern:
        new_posssible_mirrors = []
        for mirror in possible_mirrors:
            (first, second) = (mirror[0], mirror[1])
            max_extend_length = min(mirror[0], line_length - mirror[1] - 1)
            if line[first] != line[second]:
                continue
            should_append = True
            for i in range(1, max_extend_length + 1):
                if line[first - i] != line[second + i]:
                    should_append = False
                    break
            if should_append:
                new_posssible_mirrors.append((first, second))

        possible_mirrors = new_posssible_mirrors
        if len(possible_mirrors) == 0:
            return 0

    return possible_mirrors[0][0] + 1


def checkMirrors(pattern):
    ans = 0
    ans += checkVerticalMirror(pattern)
    rotated_matrix = list(
        map(lambda x: "".join(x), [*zip(*pattern)][::-1])
    )  # unholy matrix rotation counterclockwise with strings

    ans += checkVerticalMirror(rotated_matrix) * 100
    return ans


def p1(lines):
    ans = 0
    pattern = []
    for line in lines:
        if len(line) == 0:
            ans += checkMirrors(pattern)
            pattern = []
            continue
        pattern += [line]
    ans += checkMirrors(pattern)
    return ans

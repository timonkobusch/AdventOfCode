import copy
from functools import cache


@cache
def generatePossibleMirrors(lineLength):
    return list(zip(range(lineLength - 1), range(1, lineLength)))


@cache
def findPossibleMirrors(line):
    line_length = len(line)
    all_mirrors = generatePossibleMirrors(line_length)
    possible_mirrors = []
    for mirror in all_mirrors:
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
            possible_mirrors.append((first, second))
    return possible_mirrors


def checkVerticalMirror(pattern, original_tuple=None):
    line_length = len(pattern[0])
    all_possible_mirrors = generatePossibleMirrors(line_length)  # (0,1) (1,2) (2,3)

    for line in pattern:
        possible_mirrors = findPossibleMirrors(line)  # (1,2) (2,3)
        all_possible_mirrors = [
            mirror for mirror in all_possible_mirrors if mirror in possible_mirrors
        ]
        if len(all_possible_mirrors) == 0:
            return 0
    if (
        original_tuple
        and all_possible_mirrors[0][0] == original_tuple[0][0]
        and all_possible_mirrors[0][1] == original_tuple[0][1]
    ):
        if len(all_possible_mirrors) != 1:
            return all_possible_mirrors[1][0] + 1
        return 0
    return all_possible_mirrors[0][0] + 1


def checkVerticalTuples(pattern):
    line_length = len(pattern[0])
    all_possible_mirrors = generatePossibleMirrors(line_length)  # (0,1) (1,2) (2,3)

    for line in pattern:
        possible_mirrors = findPossibleMirrors(line)  # (1,2) (2,3)
        all_possible_mirrors = [
            mirror for mirror in all_possible_mirrors if mirror in possible_mirrors
        ]
        if len(all_possible_mirrors) == 0:
            return 0

    return all_possible_mirrors


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


def modifyAndCheck(pattern, x, y):
    normal_tuple = checkVerticalTuples(pattern)
    rotated_temp = copy.deepcopy(pattern)
    rotated_temp = list(map(lambda x: "".join(x), [*zip(*rotated_temp)][::-1]))
    rotated_tuple = checkVerticalTuples(rotated_temp)

    original_char = pattern[y][x]
    if original_char == ".":
        new_char = "#"
    else:
        new_char = "."

    modified_line = pattern[y][:x] + new_char + pattern[y][x + 1 :]
    modified_pattern = pattern[:y] + [modified_line] + pattern[y + 1 :]
    result = checkVerticalMirror(modified_pattern, normal_tuple)
    ans = result

    rotated_matrix = list(
        map(lambda x: "".join(x), [*zip(*modified_pattern)][::-1])
    )  # unholy matrix rotation counterclockwise with strings

    result = checkVerticalMirror(rotated_matrix, rotated_tuple)
    ans += result * 100

    return ans


def findSmudge(pattern):
    for y in range(len(pattern)):
        for x in range(len(pattern[0])):
            original = copy.deepcopy(pattern)
            ans = modifyAndCheck(pattern, x, y)
            pattern = original
            if ans != 0:
                return ans


def p2(lines):
    ans = 0
    pattern = []
    for line in lines:
        if len(line) == 0:
            ans += findSmudge(pattern)
            pattern = []
            continue
        pattern += [line]
    ans += findSmudge(pattern)
    return ans

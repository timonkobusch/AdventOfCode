from functools import cache
from typing import Tuple


# python main.py --sample true --year 2023 12
@cache
def possible(string, groups: Tuple) -> bool:
    if len(string) == 0:
        if len(groups) == 0:
            return 1
        else:
            return 0
    if len(groups) == 0:
        if "#" in string:
            return 0
        return 1

    if sum(groups) + len(groups) - 1 > len(string):
        return 0
    if string[0] == ".":
        return possible(string[1:], groups)
    if string[0] == "#":
        while groups[0] > 0:
            if string[0] == ".":
                return 0
            string = string[1:]
            groups = (groups[0] - 1,) + groups[1:]

        groups = groups[1:]
        if len(string) != 0:
            if string[0] == "#":
                return 0
            string = "." + string[1:]
            return possible(string, groups)

        return possible(string, groups)

    if string[0] == "?":
        a = "#" + string[1:]
        b = "." + string[1:]
        return possible(a, groups) + possible(b, groups)


def p1(lines):
    ans = 0
    for line in lines:
        string, group = line.split(" ")
        groups = tuple(int(x) for x in group.split(","))
        ans += possible(string, groups)

    return ans


def p2(lines):
    ans = 0
    for idx, line in enumerate(lines):
        string, group = line.split(" ")
        string = "?".join([string] * 5)
        group = ",".join([group] * 5)
        groups = tuple(int(x) for x in group.split(","))
        ans += possible(string, groups)
    return ans

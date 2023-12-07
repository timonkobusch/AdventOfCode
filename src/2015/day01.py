
def p1(line):
    count = 0
    for c in line[0]:
        if c == '(':
            count += 1
        else:
            count -= 1
    return count


def p2(line):
    count = 0
    for i, c in enumerate(line[0]):
        if c == '(':
            count += 1
        else:
            count -= 1
        if count == -1:
            return i + 1
    return -2

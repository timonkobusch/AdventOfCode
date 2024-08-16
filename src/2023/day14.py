def p1(lines):
    lastLine = [0] * len(lines[0])
    ans = 0
    for line_index, line in enumerate(lines):
        for col_index, stone in enumerate(line):
            if stone == "#":
                lastLine[col_index] = 0
            elif stone == ".":
                lastLine[col_index] += 1
            else:
                ans += len(lines) - line_index + lastLine[col_index]
    return ans


def throwNorth(lines):
    lastLine = [0] * len(lines[0])
    ans = 0
    for line_index, line in enumerate(lines):
        for col_index, stone in enumerate(line):
            if stone == "#":
                lastLine[col_index] = 0
            elif stone == ".":
                lastLine[col_index] += 1
            else:
                throw_depth = lastLine[col_index]
                ans += len(lines) - line_index + throw_depth
                current_line = list(lines[line_index])
                current_line[col_index] = "."
                lines[line_index] = "".join(current_line)

                new_line = list(lines[line_index - throw_depth])
                new_line[col_index] = "O"
                lines[line_index - throw_depth] = "".join(new_line)
    return ans


def rotateMatrix(matrix):
    return ["".join(row) for row in zip(*matrix[::-1])]


def calculateWeight(lines):
    weight = 0
    for index, line in enumerate(lines):
        for char in line:
            if char == "O":
                weight += len(lines) - index
    return weight


def doOneCycle(lines):
    for _ in range(4):
        throwNorth(lines)
        lines = rotateMatrix(lines)
    return lines


seen = {}


def p2(lines):
    N = 1000000000
    for i in range(N):
        hash = ",".join(lines)
        if hash in seen:
            cycle_length = i - seen[hash][1]
            cycles_to_go = (N - i) % cycle_length
            for _ in range(cycles_to_go):
                lines = doOneCycle(lines)
            break

        lines = doOneCycle(lines)

        seen[hash] = [hash, i]
    return calculateWeight(lines)

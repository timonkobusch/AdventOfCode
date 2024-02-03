

def p1(lines):
    def getChildNodes(node):
        y, x = node
        symbol = grid[y][x]
        children = []
        if x-1 > 0 and str(grid[y][x-1]) in "-LF":
            if symbol == 'S' or symbol == '-' or symbol == 'J' or symbol == '7':
                children.append((y, x-1))
        if x+1 < len(grid[0]) and str(grid[y][x+1]) in "-7J":
            if symbol == 'S' or symbol == '-' or symbol == 'L' or symbol == 'F':
                children.append((y, x+1))
        if y-1 > 0 and str(grid[y-1][x]) in "|F7":
            if symbol == 'S' or symbol == '|' or symbol == 'L' or symbol == 'J':
                children.append((y-1, x))
        if y+1 < len(grid) and str(grid[y+1][x]) in "|JL":
            if symbol == 'S' or symbol == '|' or symbol == 'F' or symbol == '7':
                children.append((y+1, x))

        return children

    grid = [[*x] for x in lines]
    queue = []
    start = None
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                start = (y, x)
                break

    queue.append((start, 0))
    visited = dict()
    visited[start] = (0, None)
    while len(queue) != 0:
        node, distance = queue.pop(0)
        for child in getChildNodes(node):
            if child not in visited:
                queue.append((child, distance + 1))
                visited[child] = (distance + 1, node)
    return list(visited.values())[-1]


def p2(lines):
    def getChildNodes(node):
        y, x = node
        symbol = grid[y][x]
        children = []
        if x-1 > 0 and str(grid[y][x-1]) in "-LF":
            if symbol == 'S' or symbol == '-' or symbol == 'J' or symbol == '7':
                children.append((y, x-1))
        if x+1 < len(grid[0]) and str(grid[y][x+1]) in "-7J":
            if symbol == 'S' or symbol == '-' or symbol == 'L' or symbol == 'F':
                children.append((y, x+1))
        if y-1 > 0 and str(grid[y-1][x]) in "|F7":
            if symbol == 'S' or symbol == '|' or symbol == 'L' or symbol == 'J':
                children.append((y-1, x))
        if y+1 < len(grid) and str(grid[y+1][x]) in "|JL":
            if symbol == 'S' or symbol == '|' or symbol == 'F' or symbol == '7':
                children.append((y+1, x))

        return children

    grid = [[*x] for x in lines]
    start = None
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                start = (y, x)
                break

    stack = [(90, 62)]
    visited = set()
    while len(stack) != 0:
        node = stack.pop(0)
        if node in visited:
            continue
        visited.add(node)
        for child in getChildNodes(node):
            if child not in visited:
                stack.append(child)
    print(start)
    def count_inversions(y, x):
        count = 0
        for i in range(x):
            if not (y, i) in visited:
                continue
            count += grid[y][i] in {"J", "L", "|"}
        return count

    ans = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (y, x) not in visited:
                invs = count_inversions(y, x)
                if invs % 2 == 1:
                    ans += 1

    return ans
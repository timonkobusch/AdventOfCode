

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
    visited[start] = 0
    while len(queue) != 0:
        node, distance = queue.pop(0)
        for child in getChildNodes(node):
            if child not in visited:
                queue.append((child, distance + 1))
                visited[child] = distance + 1
    return list(visited.values())[-1]
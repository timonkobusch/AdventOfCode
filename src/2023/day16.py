seen = {}


def addDirection(x, y, direction):
    if direction == 0:
        y -= 1
    elif direction == 2:
        y += 1
    elif direction == 1:
        x -= 1
    else:
        x += 1
    return (x, y)


# 0 north, 1 west, 2 south, 3 east
def followBeam(x, y, direction, tiles):
    stack = [(x, y, direction)]

    while stack:
        x, y, direction = stack.pop()

        # todo: check bounds
        if x < 0 or x >= len(tiles[0]) or y < 0 or y >= len(tiles):
            continue

        hash = str(x) + "," + str(y)
        if hash in seen and direction in seen[hash]:
            continue
        if hash not in seen:
            seen[hash] = set()

        seen[hash].add(direction)
        tile = tiles[y][x]
        if tile == ".":
            x, y = addDirection(x, y, direction)
            stack.append((x, y, direction))
        elif tile == "|":
            if direction in [0, 2]:
                x, y = addDirection(x, y, direction)
                stack.append((x, y, direction))
            else:
                stack.append((x, y + 1, 2))
                stack.append((x, y - 1, 0))
        elif tile == "-":
            if direction in [1, 3]:
                x, y = addDirection(x, y, direction)
                stack.append((x, y, direction))
            else:
                stack.append((x + 1, y, 3))
                stack.append((x - 1, y, 1))
        elif tile == "/":
            if direction == 0:
                stack.append((x + 1, y, 3))
            elif direction == 1:
                stack.append((x, y + 1, 2))
            elif direction == 2:
                stack.append((x - 1, y, 1))
            elif direction == 3:
                stack.append((x, y - 1, 0))
        elif tile == "\\":
            if direction == 0:
                stack.append((x - 1, y, 1))
            elif direction == 1:
                stack.append((x, y - 1, 0))
            elif direction == 2:
                stack.append((x + 1, y, 3))
            elif direction == 3:
                stack.append((x, y + 1, 2))

    return


def p1(tiles):
    seen.clear()
    followBeam(0, 0, 3, tiles)
    return len(seen)


def p2(tiles):
    highest_config = 0
    for y in range(len(tiles)):
        for x in range(len(tiles[0])):
            seen.clear()
            if x == 0:
                followBeam(x, y, 3, tiles)
                highest_config = max(highest_config, len(seen))
            elif x == len(tiles[0]) - 1:
                followBeam(x, y, 1, tiles)
                highest_config = max(highest_config, len(seen))
            seen.clear()
            if y == 0:
                followBeam(x, y, 2, tiles)
                highest_config = max(highest_config, len(seen))
            elif y == len(tiles) - 1:
                followBeam(x, y, 0, tiles)
                highest_config = max(highest_config, len(seen))
    return highest_config

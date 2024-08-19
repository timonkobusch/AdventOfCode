from queue import PriorityQueue


def visitNodes(lines, min_walk, max_walk):
    # init distances
    pq = PriorityQueue()
    max_x = len(lines[0]) - 1
    max_y = len(lines) - 1
    target = (max_x, max_y)

    pq.put((0, (0, 0, 0)))
    pq.put((0, (0, 0, 1)))

    seen = set()

    while pq:
        loss, (x, y, direction) = pq.get()
        if (x, y) == target:
            return loss
        if (x, y, direction) in seen:
            continue

        seen.add((x, y, direction))

        orginal_loss = loss
        for s in [-1, 1]:
            loss = orginal_loss
            new_y, new_x = y, x
            for i in range(1, max_walk + 1):
                if direction == 1:
                    new_x = x + i * s
                else:
                    new_y = y + i * s
                if new_x < 0 or new_y < 0 or new_x > max_x or new_y > max_y:
                    break
                loss += int(lines[new_y][new_x])
                new_direction = 0 if direction == 1 else 1
                if ((new_x, new_y, new_direction)) in seen:
                    continue
                if i >= min_walk:
                    pq.put((loss, (new_x, new_y, new_direction)))


def p1(lines):
    return visitNodes(lines, 1, 3)


def p2(lines):
    return visitNodes(lines, 4, 10)

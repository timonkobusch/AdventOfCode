def p1(lines):
    dirs = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
    points = [(0, 0)]

    x, y = 0, 0
    B = 0
    for line in lines:
        direction, steps, _ = line.split(" ")
        steps = int(steps)
        B += steps
        dx, dy = dirs[direction]
        x, y = (x + dx * steps, y + dy * steps)
        points.append((x, y))
    # shoelace formula: A = 0.5 * sum x_i * y_i+1 - y_i * x_i+1
    A = 0
    for i in range(len(points)):
        x_i, y_i = points[i]
        if i == len(points) - 1:
            x_i1, y_i1 = points[0]
        else:
            x_i1, y_i1 = points[i + 1]
        A += x_i * y_i1 - x_i1 * y_i
    A = A // 2

    # picks theorem, inside shape area without the edge
    I = A - (B // 2) + 1  # noqa: E741

    return I + B


def p2(lines):
    # 0 = R, 1 = D, 2 = L, 3 = U
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    points = [(0, 0)]

    x, y = 0, 0
    B = 0
    for line in lines:
        # R 6 (#70c710)
        hex_number = line.split(" ")[2]
        direction = int(hex_number[-2])
        steps = int(hex_number[2:-2], 16)

        B += steps
        dx, dy = dirs[direction]
        x, y = (x + dx * steps, y + dy * steps)
        points.append((x, y))

    A = 0
    for i in range(len(points)):
        x_i, y_i = points[i]
        if i == len(points) - 1:
            x_i1, y_i1 = points[0]
        else:
            x_i1, y_i1 = points[i + 1]
        A += x_i * y_i1 - x_i1 * y_i
    A = A // 2

    I = A - (B // 2) + 1  # noqa: E741

    return I + B

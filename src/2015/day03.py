
def p1(lines):
    houses = set()
    houses.add((0,0))
    x, y = 0, 0
    for c in lines[0]:
        if c == '^':
            y -= 1
        elif c == '>':
            x += 1
        elif c == 'v':
            y += 1
        else:
            x -= 1

        houses.add((x,y))

    return len(houses)

def p2(lines):
    houses = set()
    houses.add((0, 0))
    x1, y1, x2, y2 = 0, 0, 0, 0

    for i, c in enumerate(lines[0]):
        if i % 2 == 0:
            if c == '^':
                y1 -= 1
            elif c == '>':
                x1 += 1
            elif c == 'v':
                y1 += 1
            else:
                x1 -= 1
        else:
            if c == '^':
                y2 -= 1
            elif c == '>':
                x2 += 1
            elif c == 'v':
                y2 += 1
            else:
                x2 -= 1
        houses.add((x1, y1))
        houses.add((x2, y2))

    return len(houses)

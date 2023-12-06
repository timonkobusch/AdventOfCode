
def p1(lines):
    ans = 0
    for line in lines:
        game_number = int(line.split(':')[0].split(' ')[1])
        line = line.split(':')[1].strip().split(';')
        draws = ','.join(line).split(',')

        r ,g ,b = 0, 0, 0
        for draw in draws:
            draw = draw.strip()
            number = int(draw.split(' ')[0])
            color = draw.split(' ')[1][0]
            if color == 'r':
                r = max(r, number)
            elif color == 'g':
                g = max(g, number)
            elif color == 'b':
                b = max(b, number)
        if r <= 12 and g <= 13 and b <= 14:
            ans += game_number

    return ans


def p2(lines):
    ans = 0
    for line in lines:
        r, g, b = 0, 0, 0
        line = line.split(':')[1].strip().split(';')
        draws = ','.join(line).split(',')
        for draw in draws:
            draw = draw.strip()
            number = int(draw.split(' ')[0])
            color = draw.split(' ')[1][0]
            if color == 'r':
                r = max(r, number)
            elif color == 'g':
                g = max(g, number)
            elif color == 'b':
                b = max(b, number)
        ans += r * g * b
    return ans


def p1(lines):
    ans = 0
    for line in lines:
        (l, w, h) = (int(x) for x in line.split('x'))
        ans += 2*l*w + 2*w*h + 2*h*l + min(l*w,w*h,h*l)
    return ans


def p2(lines):
    ans = 0
    for line in lines:
        (l, w, h )= (int(x) for x in line.split('x'))
        wrap = sorted([l, w, h])
        ans += l*w*h
        ans += 2 * wrap[0] + 2 * wrap[1]
    return ans

import hashlib


def p1(lines):
    key = lines[0]
    i = 0
    while True:
        h = hashlib.md5((key + str(i)).encode()).hexdigest()
        if h.startswith('00000'):
            return i

        i += 1



def p2(lines):
    key = lines[0]
    i = 0
    while True:
        h = hashlib.md5((key + str(i)).encode()).hexdigest()
        if h.startswith('000000'):
            return i

        i += 1

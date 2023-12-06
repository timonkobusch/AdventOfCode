
def p1(lines):
    ans = 0
    for line in lines:
        digits = list(filter(lambda x: x.isdigit(), line))
        ans += int(digits[0] + digits[-1])
    return ans


def p2(lines):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    ans = 0
    for line in lines:
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits += c
            for d, val in enumerate(numbers):
                if line[i:].startswith(val):
                    digits += str(d+1)

        ans += int(digits[0] + digits[-1])
    return ans

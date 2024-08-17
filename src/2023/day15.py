def p1(lines):
    line = lines[0]
    ans = 0
    for token in line.split(","):
        current_hash = 0
        for character in token:
            current_hash += ord(character)
            current_hash *= 17
            current_hash = current_hash % 256
        ans += current_hash
    return ans


def calculateHash(token):
    ans = 0
    for char in token:
        ans += ord(char)
        ans *= 17
        ans = ans % 256
    return ans


def p2(lines):
    line = lines[0]
    boxes = [{} for _ in range(256)]
    for token in line.split(","):
        if token[len(token) - 1] == "-":
            letters = token[:-1]
            hash = calculateHash(letters)
            if letters in boxes[hash]:
                boxes[hash].pop(letters)
        else:
            letters, number = token.split("=")
            hash = calculateHash(letters)
            boxes[hash][letters] = number

    ans = 0
    for index, box in enumerate(boxes):
        for slot, lens in enumerate(box.values()):
            ans += (index + 1) * (slot + 1) * int(lens)

    return ans

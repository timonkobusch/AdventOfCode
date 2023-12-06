

def p1(lines):
    ans = 0
    for line in lines:
        line = line.split(':')[1].strip()
        winning_numbers = set(line.split('|')[0].split())
        my_ticket = set(line.split('|')[1].split())

        ticket_win = 0.5
        for number in my_ticket:
            if number in winning_numbers:
                ticket_win *= 2

        ans += int(ticket_win)

    return ans


def p2(lines):
    ans = 0
    cards_left = [1] * len(lines)
    for line_idx in range(len(lines)):
        ans += cards_left[line_idx]

        line = lines[line_idx].split(':')[1].strip()
        winning_numbers = set(line.split('|')[0].split())
        my_ticket = set(line.split('|')[1].split())

        ticket_win = len([number for number in my_ticket if number in winning_numbers])

        for i in range(1, ticket_win + 1):
            if line_idx + i < len(lines):
                cards_left[line_idx + i] += 1 * cards_left[line_idx]

    return ans

import math
import re
import itertools

def p1(lines):
    instructions = [*lines[0]]
    nav_map = {
        line.split()[0]: [re.sub(r'[(),]', '', word) for word in line.split()[2:4]]
        for line in lines[1:] if line
    }


    steps = 0
    current_state = 'AAA'
    while True:
        for instruction in instructions:
            if current_state == 'ZZZ':
                return steps

            if instruction == 'L':
                current_state = nav_map[current_state][0]
            else:
                current_state = nav_map[current_state][1]
            steps += 1

    return 0



def p2(lines):
    nav_map = {
        line.split()[0]: [re.sub(r'[(),]', '', word) for word in line.split()[2:4]]
        for line in lines[1:] if line
    }
    states = [line.split('=')[0].strip() for line in lines[1:] if line and line.split('=')[0].strip().endswith('A')]

    counts = []
    for state in states:
        steps = 0
        instructions = itertools.cycle(lines[0])

        while not state.endswith('Z'):
            steps += 1
            instruction = next(instructions)
            if instruction == 'L':
                state = nav_map[state][0]
            else:
                state = nav_map[state][1]
        counts.append(steps)

    return math.lcm(*counts)

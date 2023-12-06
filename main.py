import argparse
import importlib
import time
import datetime

import os

# input: /input/dayXX/dayXX.txt
# solution: /solution/dayXX.txt
# module: /src/dayXX.py

def read_to_list(filename, remove=False):
    output = ['', '', '', '']
    ans = ""
    part = -1
    try:
        with open(filename, 'r') as f:
            for line in f:
                if line.startswith('# Part'):
                    part += 1
                else:
                    if remove:
                        line = line.strip()
                    output[part] += line
    except FileNotFoundError:
        return output
    return output


def test_solution(day, only_sample=False, year=None):
    if day < 10:
        day = f'0{day}'
    print(year)
    if not year:
        year = datetime.date.today().year
    print(f"Day {day} Year {year}")
    # Dynamically import the day's module
    try:
        day_module = importlib.import_module(f'src.{year}.day{day}')
    except ModuleNotFoundError:
        print(f"File: 'day{day}.py' not created yet")
        return
    problem1_module = None
    problem2_module = None

    # Check if the p1 function exists in the module
    if hasattr(day_module, 'p1'):
        problem1_module = day_module.p1
    if hasattr(day_module, 'p2'):
        problem2_module = day_module.p2

    # Read the input and expected output
    input_data = read_to_list(f'input/{year}/day{day}.txt')
    expected_output = read_to_list(f'solution/{year}/day{day}.txt', remove=True)

    for i, (input, output) in enumerate(zip(input_data, expected_output)):

        if i % 2 == 0:
            part = "Sample"
        else:
            if only_sample:
                continue
            part = "Actual"
        print(f"Part {(i+2)//2} {part}:   ", end='')
        if i < 2 and problem1_module is None:
            print("| ✗ | No solution provided")
            continue
        elif i >= 2 and problem2_module is None:
            print("| ✗ | No solution provided")
            continue

        start = 0
        end = 0
        if input != '' and i < 2:
            start = time.perf_counter_ns()
            actual_output = problem1_module(input.splitlines())
            end = time.perf_counter_ns()
        elif input != '':
            start = time.perf_counter_ns()
            actual_output = problem2_module(input.splitlines())
            end = time.perf_counter_ns()
        else:
            print("| ? | No input provided")
            continue

        timer = end-start
        if output != '' and output is not None:
            if int(actual_output) == int(output):
                print(f"| ✔ | Output: {actual_output: <10} \t\t| Time: {timer:<8} Nanoseconds")
            else:
                print(f"| ✗ | Output: {actual_output:<8} != {output:<8} \t| Time: {timer:<8} Nanoseconds")
        else:
            print(f"| ? | Output: {actual_output} [No expected output provided]")



if __name__ == "__main__":
    print("Advent of Code Test")
    parser = argparse.ArgumentParser(description='Test Advent of Code solutions.')
    parser.add_argument('day', type=int, help='Day of the challenge to test')
    parser.add_argument('--sample', type=bool, nargs='?', help='Test only samples.')
    parser.add_argument('--year', type=int, nargs='?', help='Year of the problem')

    args = parser.parse_args()

    test_solution(args.day, args.sample, args.year)

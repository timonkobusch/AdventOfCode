# Advent of Code 🎄 Python Solutions & Test Framework

This repository contains my Python solutions for [Advent of Code](https://adventofcode.com/) challenges, organized by year and day.  
It includes a lightweight test framework to automatically run and validate your solutions against sample and actual inputs.


## Project Structure

.\
├── puzzle_input/ # Input files per year/day\
│ └── 2024/day01.txt\
├── expected_output/ # Expected outputs (sample + actual)\
│ └── 2024/day01.txt\
├── src/ # Your solution modules\
│ └── 2024/day01.py\
├── test.py # Main testing script


## Test Framework Usage

The `test.py` script runs your solution functions (`p1()` and `p2()`) for a given day and compares the results with expected outputs.

### Example Command


``python test.py 2024 1``


This runs both sample and actual inputs for Day 1 of 2024.

## Sample-Only Mode
``python test.py 2024 1 --sample True``

Only tests the sample inputs for quick debugging.



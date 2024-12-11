# https://adventofcode.com/2024/day/2

from common import *


def get_rows_as_int_array(filename='input.txt', separator=' '):
    lines = get_lines(filename)
    return [list(map(int, line.split(separator))) for line in lines]


def levels_are_safe(levels):
    level_change = [x - y for x, y in zip(levels[1:], levels)]
    all_increasing = all(x < 0 for x in level_change)
    all_decreasing = all(x > 0 for x in level_change)

    return (all_increasing or all_decreasing) and all(0 < abs(x) < 4 for x in level_change)


def part1():
    rows = get_rows_as_int_array()
    safe_count = 0
    for row in rows:
        if levels_are_safe(row):
            safe_count += 1
    print('Part 1:', safe_count)


def part2():
    rows = get_rows_as_int_array()
    safe_count = 0
    for row in rows:
        if levels_are_safe(row) or any(levels_are_safe(row[:i] + row[i+1:]) for i in range(len(row))):
            safe_count += 1
    print('Part 2: ', safe_count)


if __name__ == '__main__':
    part1()
    part2()

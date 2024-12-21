# https://adventofcode.com/2024/day/5

from collections import defaultdict
from common import *

ORDER_SEPARATOR = '|'
UPDATE_SEPARATOR = ','


def get_print_instructions():
    ordering = defaultdict(list)
    updates = []

    for line in get_lines(strip_newlines=True):
        if ORDER_SEPARATOR in line:
            before, after = map(int, line.split(ORDER_SEPARATOR))
            ordering[before].append(after)
        elif UPDATE_SEPARATOR in line:
            updates.append([int(x) for x in line.split(UPDATE_SEPARATOR)])

    return ordering, updates


def part1():
    ordering, updates = get_print_instructions()
    count = 0

    for update in updates:
        # for each update
        # check that pages follow the rules
        pass

    print('Part 1:', count)


def part2():
    print('Part 2:')


if __name__ == '__main__':
    part1()
    part2()

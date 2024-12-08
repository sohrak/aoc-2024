# https://adventofcode.com/2024/day/1

from collections import Counter
from common import *


def get_columns_as_int_arrays(filename='input.txt', separator='   '):
    c1 = []
    c2 = []

    for line in get_lines(filename):
        i1, i2 = map(int, line.split(separator))
        c1.append(i1)
        c2.append(i2)

    return c1, c2


def part1():
    distance = 0
    c1, c2 = get_columns_as_int_arrays()

    for i1, i2 in zip(sorted(c1), sorted(c2)):
        delta = abs(i1 - i2)
        distance += delta

    print('Part 1 distance: ', distance)


def part2():
    c1, c2 = get_columns_as_int_arrays()
    counter = Counter(c2)

    similarity = sum(i * counter.get(i, 0) for i in c1)
    print('Part 2: ', similarity)


if __name__ == '__main__':
    part1()
    part2()

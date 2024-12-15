# https://adventofcode.com/2024/day/4

from collections import defaultdict
from common import *

DIRECTIONS = [
    (-1, 0),    # left
    (1, 0),     # right
    (0, -1),    # up
    (0, 1),     # down
    (-1, -1),   # up-left
    (1, -1),    # up-right
    (-1, 1),   # down-left
    (1, 1)     # down-right
]


def is_within_bounds(i, j, max_i, max_j):
    return 0 <= i < max_i and 0 <= j < max_j


def search(grid, word, i, j, direction, max_i, max_j):
    di, dj = direction

    for c in word:
        if is_within_bounds(i, j, max_i, max_j) and c == grid[i][j]:
            i += di
            j += dj
        else:
            return False

    return True


def part1():
    count = 0

    grid = get_lines(strip_newlines=True)
    nrows = len(grid)
    ncols = len(grid[0])

    for i in range(nrows):
        for j in range(ncols):
            for direction in DIRECTIONS:
                if search(grid, 'XMAS', i, j, direction, nrows, ncols):
                    count += 1

    print('Part 1:', count)


# This is ugly but works.
def check_for_xmas(grid, i, j, max_i, max_j):
    LEFT_DIAGONAL = [(i-1, j-1), (i+1, j+1)]
    RIGHT_DIAGONAL = [(i-1, j+1), (i+1, j-1)]

    count = defaultdict(int)
    for di, dj in LEFT_DIAGONAL:
        if is_within_bounds(di, dj, max_i, max_j):
            count[grid[di][dj]] += 1

    if count['M'] != 1 or count['S'] != 1:
        return False

    count.clear()
    for di, dj in RIGHT_DIAGONAL:
        if is_within_bounds(di, dj, max_i, max_j):
            count[grid[di][dj]] += 1

    if count['M'] != 1 or count['S'] != 1:
        return False

    return True


def part2():
    count = 0

    grid = get_lines(strip_newlines=True)
    nrows = len(grid)
    ncols = len(grid[0])

    for i in range(nrows):
        for j in range(ncols):
            if grid[i][j] == 'A' and check_for_xmas(grid, i, j, nrows, ncols):
                count += 1

    print('Part 2:', count)


if __name__ == '__main__':
    part1()
    part2()

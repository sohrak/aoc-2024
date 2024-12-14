# https://adventofcode.com/2024/day/3

import re
from common import *


def part1():
    mul_sum = 0
    for line in get_lines():
        for x, y in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line):
            mul_sum += int(x) * int(y)

    print('Part 1:', mul_sum)


def part2():
    mul_sum = 0
    mul_enabled = True
    for line in get_lines():
        for mul, x, y, do, dont in re.findall(r'(mul)\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don\'t)\(\)', line):
            if mul and mul_enabled:
                mul_sum += int(x) * int(y)
            elif do:
                mul_enabled = True
            elif dont:
                mul_enabled = False

    print('Part 2:', mul_sum)


if __name__ == '__main__':
    part1()
    part2()

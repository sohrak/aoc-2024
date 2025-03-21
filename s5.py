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


def is_update_ordered(update, ordering):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            page1 = update[i]
            page2 = update[j]
            if page2 in ordering and page1 in ordering[page2]:
                return False
    return True


def topological_sort(update, ordering):
    """
    Performs a topological sort on the given update based on the ordering rules.

    Args:
        update: A list of page numbers in the update.
        ordering: A dictionary representing the ordering rules.

    Returns:
        A list of page numbers in the correct order, or None if a cycle is detected.
    """
    relevant_rules = defaultdict(list)
    in_degree = defaultdict(int)
    for before, after_list in ordering.items():
        if before in update:
            for after in after_list:
                if after in update:
                    relevant_rules[before].append(after)
                    in_degree[after] += 1

    for node in update:
        if node not in in_degree:
            in_degree[node] = 0

    queue = [node for node in update if in_degree[node] == 0]
    sorted_list = []

    while queue:
        node = queue.pop(0)
        sorted_list.append(node)

        for neighbor in relevant_rules.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(sorted_list) != len(update):
        # print('cycle detected')
        return None

    return sorted_list


def part1():
    ordering, updates = get_print_instructions()
    total_middle_page = 0

    for update in updates:
        if is_update_ordered(update, ordering):
            middle_index = len(update) // 2
            total_middle_page += update[middle_index]

    print('Part 1:', total_middle_page)


def part2():
    ordering, updates = get_print_instructions()
    total_middle_page = 0

    for update in updates:
        if not is_update_ordered(update, ordering):
            sorted_update = topological_sort(update, ordering)
            if sorted_update:
                middle_index = len(sorted_update) // 2
                total_middle_page += sorted_update[middle_index]

    print('Part 2:', total_middle_page)


if __name__ == '__main__':
    part1()
    part2()

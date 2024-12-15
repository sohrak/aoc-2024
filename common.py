# Common functions that are useful to all solutions.

def get_lines(filename='input.txt', strip_newlines=False):
    lines = None
    with open(filename, 'r') as f:
        lines = f.readlines()

    if strip_newlines:
        lines = [line.rstrip('\n') for line in lines]

    return lines

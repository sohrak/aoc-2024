# Common functions that are useful to all solutions.

def get_lines(filename='input.txt'):
    lines = None
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

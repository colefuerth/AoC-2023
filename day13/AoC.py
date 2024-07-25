#!/usr/bin/python3

import sys
from itertools import groupby, product
from copy import deepcopy
from typing import List


def horizontal(grid):
    for i in range(1, len(grid)):
        l, h = reversed(grid[:i]), grid[i:]
        m = True
        for a, b in zip(l, h):
            if a != b:
                m = False
                break
        if m:
            return i
    return 0


def part1(f: List[List[str]]) -> int:
    # only match using horizontals since they are easier
    # vertical lines can be found by transposing the grid and running a horizontal check on them
    return sum(
        horizontal(grid) * 100 for grid in f
    ) + sum(
        horizontal(list(zip(*grid))) for grid in f
    )

if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [l.strip() for l in open(fname, 'r').readlines()]
    f = [list(group) for key, group in groupby(f, lambda x: x == '') if not key]

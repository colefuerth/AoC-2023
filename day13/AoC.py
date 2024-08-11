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


def part2(f: List[str]) -> int:
    total = 0
    for i, grid in enumerate(f):
        grid = [[{'#':1, '.':0}[c] for c in line] for line in grid]
        ho, vo = horizontal(grid), horizontal(list(zip(*grid)))
        for x, y in product(range(len(grid)), range(len(grid[0]))):
            grid[x][y] ^= 1
            h, v = horizontal(grid), horizontal(list(zip(*grid)))
            grid[x][y] ^= 1
            # if h and x in range(h - min(h, len(grid) - h), h + min(h, len(grid) - h)):
            if h and h != ho:
                print(f'grid {i+1} was at {"horizontal", h} with smudge {x, y} and grid size {len(grid), len(grid[0])}')
                total += h * 100
                break
            # if v and y in range(v - min(v, len(grid[0]) - v), v + min(v, len(grid) - v)):
            if v and v != vo:
                print(f'grid {i+1} was at {("vertical", v)} with smudge {x, y} and grid size {len(grid), len(grid[0])}')
                total += v
                break
    # 26377 is too low
    return total


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [l.strip() for l in open(fname, 'r').readlines()]
    f = [list(group) for key, group in groupby(f, lambda x: x == '') if not key]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))

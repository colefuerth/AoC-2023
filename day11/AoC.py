#!/usr/bin/python3

import sys
from itertools import combinations
from copy import deepcopy
from typing import List


def expand_and_calculate(f: List[str], expansion_size: int) -> int:
    # calculate offsets
    horizontal = [0 for _ in range(len(f[0]))]
    vertical = [0 for _ in range(len(f))]
    for y, line in enumerate(f):
        for x, c in enumerate(line):
            if c == '#':
                horizontal[x] = 1
                vertical[y] = 1

    # adjust coordinates
    galaxies = []
    offset_y = 0
    for y, line in enumerate(f):
        offset_x = 0
        for x, c in enumerate(line):
            if c == '#':
                galaxies.append([x + offset_x, y + offset_y])
            if horizontal[x] == 0:
                offset_x += expansion_size - 1
        if vertical[y] == 0:
            offset_y += expansion_size - 1

    # return euclidian distances between combinations of galaxies
    return sum(abs(a[0] - b[0]) + abs(a[1] - b[1]) for a, b in combinations(galaxies, r=2))


def part1(f: List[str]) -> int:
    # part 1 just doubles empty space
    return expand_and_calculate(f, 2)


def part2(f: List[str]) -> int:
    # part 2 makes it a million times bigger
    return expand_and_calculate(f, 1000000)


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
    ]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))

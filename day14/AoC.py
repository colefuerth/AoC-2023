#!/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
from typing import List

cache = {}
def fall_north(f):
    h = sum(hash(tuple(row)) for row in f)
    if h in cache:
        return cache[h]
    for x, y in product(range(len(f)), range(len(f[0]))):
        if f[x][y] == 'O':
            dx = x - 1
            while dx >= 0 and f[dx][y] == '.':
                f[dx + 1][y], f[dx][y] = f[dx][y], f[dx + 1][y]
                dx -= 1
    cache[h] = deepcopy(f)
    return f

def north_load(f):
    mass = 0
    for x, y in product(range(len(f)), range(len(f[0]))):
        if f[x][y] == 'O':
            mass += len(f) - x
    return mass


def part1(f: List[str]) -> int:
    fall_north(f)
    return north_load(f)

def part2(f: List[str]) -> int:
    """
    the idea here is that after a while of tumbling, a pattern arises; as soon as we detect that pattern we can calculate where any future tumble will land
    """
    histogram = {}  # hash : [count, load]
    loop = []       # list of hashes in the main loop
    target = 1000000000 * 4
    for x in range(target):
        f = fall_north(f)
        f = [list(row) for row in zip(*f[::-1])]
        h = hash(''.join(''.join(j for j in i) for i in f)) + hash("nwse"[x % 4])
        if h not in histogram:
            histogram[h] = [1, north_load(f)]
        else:
            histogram[h][0] += 1
        if not loop:
            if histogram[h][0] == 2:
                first_loop = x
                loop.append(h)
        else:
            if histogram[h][0] == 3:
                break
            loop.append(h)
    return histogram[loop[(target - first_loop) % len(loop) - 1]][1]

if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        list(l.strip())
        for l in open(fname, 'r').readlines()
    ]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))

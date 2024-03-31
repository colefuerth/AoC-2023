#!/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
from typing import List

# for each line, find each integer in each line
# if there is a symbol on either side (non-'.') then it is a part number and it is added to the sum

dirs = tuple(product([-1, 0, 1], repeat=2))

add_coords = lambda x, y: (x[0] + y[0], x[1] + y[1])

def part1(f: List[str]) -> int:
    # each match can be a hash of its x, y of the first digit, and its integer
    # then, each coordinate that that has a number in it can be mapped to that hash
    
    # build the tingy
    symbols = {
        (x,y)
        for x, y in product(range(len(f)), range(len(f[0])))
        if f[x][y] not in '0123456789.'
    }
    sum = 0
    for i, line in enumerate(f):
        for match in re.finditer(r'(\d+)', line):
            for coord in [(i, j) for j in range(match.start(), match.end())]:
                if any(add_coords(coord, d) in symbols for d in dirs):
                    sum += int(match.group(1))
                    break
    return sum

            
def part2(f: List[str]) -> int:
    # find all the asterisks
    gears = [
        (x,y)
        for x, y in product(range(len(f)), range(len(f[0])))
        if f[x][y] == '*'
    ]
    # parse the ints and locations in the engine map
    nums = {}  # map from coords to hash
    ints = {}  # map from hash to ints
    for i, line in enumerate(f):
        for match in re.finditer(r'(\d+)', line):
            for coord in [(i, j) for j in range(match.start(), match.end())]:
                h = hash((i, match.start(), int(match.group(1))))
                nums[coord] = h
                ints[h] = int(match.group(1))
    # figure out which asterisks are gears, and update the sum when they are found
    sum = 0
    for g in gears:
        adj = []
        for d in dirs:
            dx = add_coords(g, d)
            if dx in nums and nums[dx] not in adj:
                adj.append(nums[dx])
        if len(adj) == 2:
            sum += ints[adj[0]] * ints[adj[1]]
                
    return sum


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
        if l.strip() != ''
    ]

    print('Part 1:', part1(f))
    print('Part 2:', part2(f))

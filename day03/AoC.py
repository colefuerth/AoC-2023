#!/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
from typing import List

# for each line, find each integer in each line
# if there is a symbol on either side (non-'.') then it is a part number and it is added to the sum

dirs = (
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
)

add_coords = lambda x, y: (x[0] + y[0], x[1] + y[1])

def part1(f: List[str]) -> int:
    # each match can be a hash of its x, y of the first digit, and its integer
    # then, each coordinate that that has a number in it can be mapped to that hash
    
    # build the tingy
    coords = {
        (x,y):f[x][y] if f[x][y] != '.' else None
        for x, y in product(range(len(f)), range(len(f[0])))
    }
    ints = {}  # each hash is mapped to an integer value for summing later
    hist = {}  # each hash is mapped to a count of "hits", >0 means it is a part number
    for i, line in enumerate(f):
        for match in re.finditer(r'(\d+)', line):
            h = hash(match)
            ints[h] = int(match.group(1))
            hist[h] = 0
            for coord in [(i, j) for j in range(match.start(), match.end())]:
                coords[coord] = h
    
    # traverse the tingy
    for coord in coords:
        if isinstance(coords[coords[coord]], str):
            # for each direction, traverse until either hitting a wall or another object
            for d in dirs:
                c = add_coords(c, d)
                while c in coords:
                    if coords[c] != None:
                        if isinstance(coords[c], int):
                            hist[coords[c]] += 1
                        break
    return sum([ints[h] for h, c in hist.items() if c > 0])
            
    # find the two hashes that have the same count

def part2(f: List[str]) -> int:
    pass


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
        if l.strip() != ''
    ]

    print('Part 1:', part1(f))
    print('Part 2:', part2(f))

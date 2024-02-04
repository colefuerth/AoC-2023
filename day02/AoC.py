#!/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
from typing import List
from math import prod


def part1(f: List[str]) -> int:
    bag = {"red":12, "green":13, "blue":14}
    sum = 0
    for i, game in enumerate(f):
        possible = True
        game = re.sub(r"Game \d+: ", "", game)
        for group in game.split("; "):
            cubes = group.split(", ")
            for cube in cubes:
                n, c = cube.split(" ")
                if bag[c] - int(n) < 0:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            sum += i + 1
    return sum

def part2(f: List[str]) -> int:
    sum = 0
    for i, game in enumerate(f):
        bag = {"red":0, "green":0, "blue":0}
        game = re.sub(r"Game \d+: ", "", game)
        for group in game.split("; "):
            cubes = group.split(", ")
            for cube in cubes:
                n, c = cube.split(" ")
                bag[c] = max(bag[c], int(n))
        sum += prod(bag.values())
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

#!/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
from typing import List

def holiday_ascii_string_helper(s: str):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256
    return h


def part1(f: List[str]) -> int:
    f = ''.join(f).split(',')
    return sum(holiday_ascii_string_helper(s) for s in f)


def part2(f: List[str]) -> int:
    pass


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
    ]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))

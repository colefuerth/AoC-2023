#!/usr/bin/python3

import sys
from copy import deepcopy
from typing import List, Dict


def match_pattern(s: str, p: List[int], cache: Dict[tuple, int]):
    # base case is empty string
    if s == '':
        if len(p) == 0:
            return 1
        return 0
    # if begin with whitespace, then clear it
    if s[0] == '.':
        while s != '' and s[0] == '.':
            s = s[1:]
        return match_pattern(s, deepcopy(p), cache)
    # check cache
    h = (s, tuple(p))
    if h in cache:
        return cache[h]
    # remove ambiguity
    if s[0] == '?':
        cache[h] = match_pattern('#' + s[1:], deepcopy(p), cache) + match_pattern(s[1:], deepcopy(p), cache)
        return cache[h]
    # end of string condition
    if len(s) == 1:
        if s == '#' and len(p) == 1 and p[0] == 1:
            cache[h] = 1
            return 1
        cache[h] = 0
        return 0
    # remove ambiguity for lookahead
    if s[1] == '?':
        cache[h] = match_pattern(s[0] + '#' + s[2:], deepcopy(p), cache) + match_pattern(s[0] + '.' + s[2:], deepcopy(p), cache)
        return cache[h]
    # check continue conditions
    if s[0] == '#' and s[1] == '#' and len(p) > 0 and p[0] > 0:
        p[0] -= 1
        s = s[1:]
    elif s[0] == '#' and s[1] == '.' and len(p) > 0 and p[0] == 1:
        p = p[1:]
        s = s[2:]
    else:
        cache[h] = 0
        return 0
    # continue to next state
    cache[h] = match_pattern(s, deepcopy(p), cache)
    return cache[h]
            

def part1(f: List[str]) -> int:
    return sum(match_pattern(s, deepcopy(p), {}) for s, p in f)


def part2(f: List[str]) -> int:
    return sum(match_pattern('?'.join([s]*5), p * 5, {}) for s, p in f)


if __name__ == '__main__':
    # fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    fname = sys.argv[1] if len(sys.argv) > 1 else '/home/cole/AoC-2023/day12/small.txt'
    f = [
        l.strip().split()
        for l in open(fname, 'r').readlines()
    ]
    f = [[l[0], [int(i) for i in l[1].split(',')]] for l in f]
    
    # print(f)

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))

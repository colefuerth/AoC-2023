#!/usr/bin/python3

import sys
import re
from typing import List


def part1(f: List[str]) -> int:
    sum = 0
    for m in re.findall(r"(\d+\s*(?:\d+\s*)*)\s*\|\s*(\d+\s*(?:\d+\s*)*)", '\n'.join(f)):
        c = len(m[1].split()) - len(set(map(int, m[1].split())) - set(map(int, m[0].split())))
        if c > 0:
            sum += 2 ** (c - 1)
    return sum
        

def part2(f: List[str]) -> int:
    cards = []
    for m in re.findall(r"(\d+\s*(?:\d+\s*)*)\s*\|\s*(\d+\s*(?:\d+\s*)*)", '\n'.join(f)):
        c = len(m[1].split()) - len(set(map(int, m[1].split())) - set(map(int, m[0].split())))
        cards.append([1, c])
    sum = 0
    for i, (count, wins) in enumerate(cards):
        sum += count
        for cp in cards[i + 1 : i + 1 + wins]:
            cp[0] += count
        
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

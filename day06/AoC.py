#!/usr/bin/python3

import sys
from typing import List

# full disclosure I am tired and this whole problem can be brute forced in about 5 seconds so that is what I will do
# I will also note that I am well aware there is a constant time solution you can do by plotting the relation and finding the roots but today is not that day

def part1(f: List[List[int]]) -> int:
    prod = 1
    for t, d in zip(*f):
        sum = 0
        for dt in range(1, t):
            if dt * (t - dt) > d:
                sum += 1
        prod *= sum
    return prod


def part2(f: List[List[int]]) -> int:
    f = [[int(''.join(map(str, l))),] for l in f]
    
    return part1(f)


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        [int(i) for i in l.split(':')[1].split()]
        for l in open(fname, 'r').readlines()
    ]

    print('Part 1:', part1(f))
    print('Part 2:', part2(f))

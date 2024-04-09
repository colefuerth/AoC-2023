#!/usr/bin/python3

import sys
from copy import deepcopy
from typing import List


def part1(f: List[str]) -> int:
    for sequence in f:
        diffs = [sequence]
        while any(i != 0 for i in diffs[-1]):
            diffs.append(
                [b - a for a, b in zip(diffs[-1][:-1], diffs[-1][1:])]
            )
        for diff, seq in zip(diffs[:0:-1], diffs[-2::-1]):
            seq.append(diff[-1] + seq[-1])
    return sum([seq[-1] for seq in f])

def part2(f: List[str]) -> int:
    for sequence in f:
        diffs = [sequence]
        while any(i != 0 for i in diffs[-1]):
            diffs.append(
                [b - a for a, b in zip(diffs[-1][:-1], diffs[-1][1:])]
            )
        for diff, seq in zip(diffs[:0:-1], diffs[-2::-1]):
            seq.insert(0, seq[0] - diff[0])
    return sum([seq[0] for seq in f])


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        [int(i) for i in l.split()]
        for l in open(fname, 'r').readlines()
    ]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))

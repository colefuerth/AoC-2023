#!/usr/bin/python3

import sys
from copy import deepcopy
import re
from typing import List
from math import lcm


def part1(f: List[str]) -> int:
    instructions = [0 if c == 'L' else 1 for c in f[0]]
    nodes = {match[0]:tuple(match[1:]) for match in [re.findall(r'[A-Z]+', line) for line in f[2:]]}
    
    steps = 0
    acc = 'AAA'
    
    while acc != 'ZZZ':
        acc = nodes[acc][instructions[steps % len(instructions)]]
        steps += 1
    return steps

def part2(f: List[str]) -> int:
    instructions = [0 if c == 'L' else 1 for c in f[0]]
    nodes = {match[0]:tuple(match[1:]) for match in [re.findall(r'[0-9A-Z]+', line) for line in f[2:]]}
    
    steps = 0
    accs = [node for node in nodes if node[2] == 'A']
    multiples = [0 for _ in accs]
    
    while any(m == 0 for m in multiples):
        for i in range(len(accs)):
            accs[i] = nodes[accs[i]][instructions[steps % len(instructions)]]
            if accs[i][2] == 'Z':
                if multiples[i] == 0:
                    multiples[i] = steps + 1
        steps += 1
    return lcm(*multiples)


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
    ]
    
    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))

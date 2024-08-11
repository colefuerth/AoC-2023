#!/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
from typing import List

U = (0, -1)
D = (0, 1)
L = (-1, 0)
R = (1, 0)

MIRRORS = None

def isvalidcoord(coord, f):
    return True if \
        coord[0] in range(0, len(f[0])) and \
        coord[1] in range(0, len(f)) \
        else False

class Light:
    def __init__(self, vector: tuple[int, int], origin: tuple[int, int]):
        self.vector = vector
        self.location = origin
        
    def step(self, f: List[str]) -> bool:
        self.location = (self.location[0] + self.vector[0], self.location[1] + self.vector[1])
        return isvalidcoord(self.location, f)
            
    def encounter(self, char: str) -> list:
        # each new spot it lands will be an encounter
        if char in '|-':
            return self.scatter(char)
        if char in '/\\':
            return self.reflect(char)
        return [self]

    def scatter(self, char: str) -> list:
        if self.vector in (U, D) and char == '-':
            return [Light(L, self.location), Light(R, self.location)]
        if self.vector in (L, R) and char == '|':
            return [Light(U, self.location), Light(D, self.location)]
        return [self] # keep going straight if there is not a scatter condition

    def reflect(self, char: str):
        dx = {
            '/' : {
                U : R,
                D : L,
                R : U,
                L : D
            },
            '\\' : {
                U : L,
                D : R,
                L : U,
                R : D
            }
        }
        self.vector = dx[char][self.vector]
        return [self]
    
    def __str__(self) -> str:
        return f'Light pos {self.location} vec {self.vector}'


def part1(f: List[str]) -> int:
    activated = set()
    bucket = [Light(R, (-1, 0))]
    while bucket:
        # print()
        # print(f'bucket is {bucket}')
        print(f'activated is {len(activated)}')
        new_bucket = []
        for b in bucket:
            if b.step(f):
                activated.update(b.location)
                new_bucket.extend(b.encounter(f[b.location[1]][b.location[0]]))
        print()
        for y in range(len(f)):
            for x in range(len(f[y])):
                print('#' if (x, y) in activated else '.', end='')
            print()
        bucket = new_bucket
        
    print()
    for y in range(len(f)):
        for x in range(len(f[y])):
            print('#' if (x, y) in activated else '.', end='')
        print()
    return len(activated)


def part2(f: List[str]) -> int:
    pass


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else '/home/cole/AoC-2023/day16/small.txt'
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
    ]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))

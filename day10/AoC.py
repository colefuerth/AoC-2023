#!/usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
from typing import List, Tuple
from math import ceil

# each pipe is mapped to a map of input directions and their resulting output direction
RIGHT = (0, 1)
LEFT = (0, -1)
UP = (-1, 0)
DOWN = (1, 0)
dirs = (RIGHT, DOWN, LEFT, UP)
pipes = {
    '|':{DOWN:DOWN, UP:UP},
    '-':{RIGHT:RIGHT, LEFT:LEFT},
    'F':{UP:RIGHT, LEFT:DOWN},
    '7':{RIGHT:DOWN, UP:LEFT},
    'J':{RIGHT:UP, DOWN:LEFT},
    'L':{DOWN:RIGHT, LEFT:UP}
}


def add_coords(a: Tuple[int], b: Tuple[int]):
    return (a[0] + b[0], a[1] + b[1])

def valid_coordinate(x: int, y: int, f: List[str]):
    return x in range(len(f)) and y in range(len(f[0]))

def find_loop(f: List[str]) -> list:
    for x, y in product(range(len(f)), range(len(f[0]))):
        if f[x].find('S') != -1:
            start = (x, f[x].find('S'))
            break
    for dir in dirs:
        loop = [start]
        x, y = add_coords(dir, start)
        while valid_coordinate(x, y, f) and f[x][y] != '.' and dir in pipes[f[x][y]]:
            dir = pipes[f[x][y]][dir]
            x, y = add_coords((x, y), dir)
            if f[x][y] == 'S':
                return loop
            loop.append((x, y))

def part1(f: List[str]) -> int:
    return ceil(len(find_loop(f)) / 2)
            
expand_map = {
    '|':[' l ',' l ',' l '],
    '-':['   ','lll','   '],
    'F':['   ',' ll',' l '],
    '7':['   ','ll ',' l '],
    'J':[' l ','ll ','   '],
    'L':[' l ',' ll','   '],
    'S':[' l ','lll',' l ']
}

def part2(f: List[str]) -> int:
    # okay so my extremely cursed idea is to just,, make each 1x1 a 3x3 and then flood it and then if I delete all squares with water in them then I am just left with the ones that are inside the loop
    # only copy the pipes in the loop and use them as walls
    # flood at the outer loop
    
    # first, create the extended arena
    loop = set(find_loop(f))
    fe = [[' ' for _ in range(len(f[0]) * 3)] for _ in range(len(f) * 3)]
    for x, y in product(range(len(f)), range(len(f[0]))):
        if (x, y) in loop:
            pattern = expand_map[f[x][y]]
            for i, j in product(range(3), range(3)):
                fe[3*x + i][3*y + j] = pattern[i][j]
    
    # now, fill the edge with water
    flooded = {}
    queue = []
    queue.extend([(0, y) for y in range(len(f[0]))])
    queue.extend([(len(fe) - 1, y) for y in range(len(fe[0]))])
    queue.extend([(x, 0) for x in range(len(fe))])
    queue.extend([(x, len(fe[0]) - 1) for x in range(len(fe))])
    
    while queue:
        new_queue = []
        flooded.update(queue)
        for q, d in product(queue, dirs):
            c = add_coords(q, d)
            if valid_coordinate(*c, fe) and fe[c[0]][c[1]] == ' ' and c not in flooded:
                new_queue.append(c)
        queue = new_queue

    count = 0
    for x, y in product(range(len(f)), range(len(f[0]))):
        if f[x][y] == '.':
            if all(add_coords((i, j), (x * 3, y * 3)) not in flooded for i, j in product(range(3), range(3))):
                count += 1
    return count

if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        l.strip()
        for l in open(fname, 'r').readlines()
    ]

    print('Part 1:', part1(deepcopy(f)))
    print('Part 2:', part2(deepcopy(f)))

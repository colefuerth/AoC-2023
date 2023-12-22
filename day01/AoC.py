# /usr/bin/python3

import sys
from itertools import product, count, permutations
from copy import deepcopy
import re
from typing import List


def part1(f: List[str]) -> int:
    r = re.compile("\d")
    sum = 0
    for line in f:
        l = r.findall(line)
        sum += int(l[0]) * 10 + int(l[-1])
    return sum


def part2(f: List[str]) -> int:
    nums = "one,two,three,four,five,six,seven,eight,nine".split(",")
    nmap = {num:i+1 for i, num in enumerate(nums)}
    nmap.update({num[::-1]:i+1 for i, num in enumerate(nums)})
    nmap.update({str(i):i for i in range(1, 10)})
    r = re.compile("|".join(nums) + r"|\d")
    rr = re.compile("|".join([s[::-1] for s in nums]) + r"|\d")
    sum = 0
    for i, line in enumerate(f):
        sum += nmap[r.search(line).group()] * 10
        sum += nmap[rr.search(line[::-1]).group()]
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

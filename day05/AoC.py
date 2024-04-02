#!/usr/bin/python3

import sys
from itertools import groupby
from copy import deepcopy
from typing import List

def seed_convert(seed: int, group: List[int]) -> int:
    for dest, src, span in group:
        if seed in range(src, src + span):
            seed += dest - src
            break
    return seed

def partition(seeds: List[List[int]], group: List[int]) -> List[List[int]]:
    for _, gsrc, gspan in group:
        gend = gsrc + gspan
        for i, (ssrc, sspan) in enumerate(seeds):
            for idx in [gsrc, gend]:
                if idx in range(ssrc + 1, ssrc + sspan):
                    seeds.insert(i, [ssrc, idx - ssrc])
                    seeds[i + 1] = [idx, sspan - (idx - ssrc)]
                    return partition(seeds, group)
    return seeds

def part1(seeds: List[int], maps: List[List[int]]) -> int:
    seed_to_location = []

    for seed in seeds:
        s = seed
        for group in maps:
            s = seed_convert(s, group)
        seed_to_location.append([seed, s])
    return min(seed_to_location, key=lambda x: x[1])[1]

def part2(seeds: List[int], maps: List[List[int]]) -> int:
    seeds = [[seed, span] for seed, span in zip(seeds[::2], seeds[1::2])]

    for group in maps:
        seeds = partition(seeds, group)
        for seed in seeds:
            seed[0] = seed_convert(seed[0], group)
    return min(seeds, key=lambda x: x[0])[0]

if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [l.strip() for l in open(fname, 'r').readlines()]

    seeds = [int(s) for s in f[0][7:].split()]
    maps = []
    for group in [list(group) for key, group in groupby(f[2:], lambda x: x == '') if not key]:
        maps.append(
            tuple(tuple(map(int, m)) for m in list(map(str.split, group[1:])))
        )
    maps = tuple(maps)
    
    print('Part 1:', part1(deepcopy(seeds), maps))
    print('Part 2:', part2(seeds, maps))

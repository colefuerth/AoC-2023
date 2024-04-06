#!/usr/bin/python3

import sys
from typing import List
from collections import Counter as histogram
from functools import cmp_to_key
from itertools import product


def part1(f: List[List[str]]) -> int:
    cards = '23456789TJQKA'
    hands = [[1, 1, 1, 1, 1], [2, 1, 1, 1], [2, 2, 1], [3, 1, 1], [3, 2], [4, 1], [5]]

    def compareHands(a: str, b: str) -> int:
        # a < b: -1, a = b: 0, a > b: 1
        seq_a = hands.index(sorted(histogram(a).values(), reverse=True))
        seq_b = hands.index(sorted(histogram(b).values(), reverse=True))
        if seq_a < seq_b:
            return -1
        if seq_a > seq_b:
            return 1
        for ca, cb in zip(a, b):
            if cards.index(ca) < cards.index(cb):
                return -1
            if cards.index(ca) > cards.index(cb):
                return 1
        return 0
    f = sorted(f, key=cmp_to_key(lambda a, b: compareHands(a[0], b[0])))
    
    return sum([int(s[1]) * (i + 1) for i, s in enumerate(f)])


def part2(f: List[List[str]]) -> int:
    cards = 'J23456789TQKA'
    hands = [[1, 1, 1, 1, 1], [2, 1, 1, 1], [2, 2, 1], [3, 1, 1], [3, 2], [4, 1], [5]]
    
    def bestHand(hand: str) -> int:
        jcount = hand.count('J')
        if jcount == 0:
            return hands.index(sorted(histogram(hand).values(), reverse=True))
        best = 0
        for prod in product(cards[1:], repeat=jcount):
            h = hand
            for p in prod:
                h = h.replace('J', p, 1)
            best = max(best, hands.index(sorted(histogram(h).values(), reverse=True)))
        return best
            
    hand_cache = {hand:bestHand(hand) for hand, _ in f}

    def compareHands(a: str, b: str) -> int:
        # a < b: -1, a = b: 0, a > b: 1
        if hand_cache[a] < hand_cache[b]:
            return -1
        if hand_cache[a] > hand_cache[b]:
            return 1
        for ca, cb in zip(a, b):
            if cards.index(ca) < cards.index(cb):
                return -1
            if cards.index(ca) > cards.index(cb):
                return 1
        return 0
    f = sorted(f, key=cmp_to_key(lambda a, b: compareHands(a[0], b[0])))
    
    return sum([int(s[1]) * (i + 1) for i, s in enumerate(f)])


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    f = [
        l.strip().split()
        for l in open(fname, 'r').readlines()
    ]

    print('Part 1:', part1(f))
    print('Part 2:', part2(f))

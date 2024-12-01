#!/usr/bin/env python

import sys


def get_lists():
    a = []
    b = []
    with open('%s/input' % sys.path[0]) as f:
        for line in f:
            l = line.strip().replace('   ', ',').split(',')
            a.append(int(l[0]))
            b.append(int(l[1]))
            a.sort()
            b.sort()
    return (a, b)

def get_pairs():
    a, b  = get_lists()
    return zip(a,b)


def part1():
    pairs = get_pairs()
    return sum(map(lambda pair: abs(pair[1] - pair[0]), pairs))


def part2():
    counter = {}
    a, b = get_lists()
    for i in b:
        counter[i] = counter.pop(i, 0) + 1
    return sum(map(lambda x: counter.get(x, 0) * x, a))


print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')

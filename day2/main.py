#!/usr/bin/env python

import sys

def get_reports():
    with open('%s/input' % sys.path[0]) as f:
        l = [line.strip().split(' ') for line in f]
        return [list(map(lambda x: int(x), a)) for a in l]


def is_safe(report):
    r = list(map(lambda p: p[1] - p[0], zip(report, report[1:])))

    if all(x < 0 and 1 <= abs(x) <= 3 for x in r):
        return True
    if all(1 <= x <= 3 for x in r):
        return True
    return False


def part1():
    return len(list(filter(is_safe, get_reports())))


def p2_safe(report):
    return any(is_safe(report[:i] + report[i + 1:]) for i in range(len(report)))


def part2():
    return len(list(filter(p2_safe, get_reports())))


print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')

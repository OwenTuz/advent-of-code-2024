#!/usr/bin/env python

import sys


def is_valid(target, operands, p2=False):
    *rest, n = operands
    if not rest:
        return n == target
    quotient, remainder = divmod(target, n)
    if remainder == 0 and is_valid(quotient, rest, p2):
        return True
    if p2:
        str_target = str(target)
        str_n = str(n)
        if str_target.endswith(str_n) and is_valid(target // (10 ** len(str_n)), rest, p2):
            return True
    return is_valid(target - n, rest, p2)


def part1(data):

    total = 0
    for line in data:
        target, *operands = line
        if is_valid(target, operands):
            total = total + target

    return total

def part2(data):
    total = 0
    for line in data:
        target, *operands = line
        if is_valid(target, operands, True):
            total = total + target

    return total

with open('%s/input' % sys.path[0]) as f:
    data = [list(map(int, line.strip().replace(':', '').split())) for line in f]
print(f'Part 0: {part1(data)}')
print(f'Part 2: {part2(data)}')

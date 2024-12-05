#!/usr/bin/env python

import sys
from collections import defaultdict

def parse():
    rules = defaultdict(list)
    updates = []
    with open('%s/input' % sys.path[0]) as f:
        for line in (line.strip() for line in f):
            if '|' in line:
                l = line.split('|')
                rules[l[0]].append(l[1])
            if ',' in line:
                updates.append(line.split(','))
    return (rules, updates)


def part1():
    rules, updates = parse()
    total = 0
    for update in updates:
        for i, n in enumerate(update):
            if any(x in update[:i] for x in rules[n]):
                break
        else:
            total = total + int(update[len(update) // 2])
    return total

def sort(rules, update):
    for i, n in enumerate(update):
        if any(x in update[:i] for x in rules[n]):
            for j in range(i):
                if update[j] in rules[n]:
                    del update[i]
                    update.insert(j, n)
                    return sort(rules, update)
    return update



def part2():
    rules, updates = parse()
    total = 0
    for update in updates:
        for i, n in enumerate(update):
            if any(x in update[:i] for x in rules[n]):
                total = total + int(sort(rules, update)[len(update) // 2])
                break
    return total

print(f'Part 1: {part1()}')
print(f'Part 1: {part2()}')

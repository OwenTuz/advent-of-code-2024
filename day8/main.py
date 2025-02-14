#!/usr/bin/env python

import sys
from itertools import permutations

def part1():
    with open('%s/input' % sys.path[0]) as f:
        grid = {
            i + k*1j: v for i, row in enumerate(f)
                        for k, v in enumerate(row.strip())
        }

    antinodes = set()
    for freq in set(grid.values()) - {'.'}:
        pairs = permutations([i for i in grid if grid[i] == freq], 2)
        for a,b in pairs:
            if (candidate := a + (a - b)) in grid:
                antinodes.add(candidate)

    return len(antinodes)

def part2():
    with open('%s/input' % sys.path[0]) as f:
        grid = {i+k*1j: v for i, row in enumerate(f)
               for k, v in enumerate(row.strip())}

    antinodes = set()
    for freq in set(grid.values()) - {'.'}:
        pairs = permutations([i for i in grid if grid[i] == freq], 2)
        for a,b in pairs:
            for i in range(50): # cheating here: hardcoded input grid length
                if (candidate := a + i*(a - b)) in grid:
                    antinodes.add(candidate)

    return len(antinodes)

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')

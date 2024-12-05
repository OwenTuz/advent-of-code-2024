#!/usr/bin/env python

import sys


class WordGrid:
    def __init__(self):
        with open('%s/input' % sys.path[0]) as f:
            self.rows = [line.rstrip() for line in f]

    def try_get(self, x, y):
        """
        what happens if you impl dict.get() for a list of strings
        """
        if x < 0 or y < 0:
            return ""
        try:
            return self.rows[y][x]
        except IndexError:
            return ""


def part1():
    grid = WordGrid()
    found = 0
    word = 'XMAS'
    directions = [
        (1,0), # left->right
        (-1,0), # right->left
        (0,1), # down
        (0,-1), # up
        (1, 1), # diagonals
        (-1, 1),
        (-1, -1),
        (1, -1)
    ]
    for y in range(len(grid.rows)):
        for x in range(len(grid.rows[y])):
            if grid.rows[y][x] == word[0]:
                for dx, dy in directions:
                    candidate = ""
                    for i in range(len(word)):
                        candidate = candidate + grid.try_get(x + i * dx, y + i * dy)
                    if candidate == word:
                        found = found + 1
    return found


def part2():
    grid = WordGrid()
    found = 0
    for y in range(len(grid.rows)):
        for x in range(len(grid.rows[y])):
            if grid.rows[y][x] == 'A':
                d1 = grid.try_get(x + 1, y + 1) + "A" + grid.try_get(x - 1, y - 1)
                d2 = grid.try_get(x - 1, y + 1) + "A" + grid.try_get(x + 1, y - 1)

                if (d2 == 'MAS' or d2 == 'SAM') and (d1 == 'MAS' or d1 == 'SAM'):
                    found = found + 1
    return found


print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')

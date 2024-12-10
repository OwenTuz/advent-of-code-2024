#!/usr/bin/env python

import sys

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class Grid:
    def __init__(self):
        self.directions = {
            UP: (0,-1),
            RIGHT: (1,0),
            DOWN: (0,1),
            LEFT: (-1,0)
        }
        self.dir = UP
        self.pos = None
        self.visited = set()
        self.loop_map = set()

        self.grid = []
        with open('%s/input' % sys.path[0]) as f:
            for i, line in enumerate(f):
                self.grid.append(line.strip())
                if '^' in line:
                    self.pos = (line.index('^'), i)

    def step(self):
        self.visited.add(self.pos)
        self.loop_map.add((self.pos, self.dir))
        x, y = self.pos
        dx, dy = self.directions[self.dir]
        target = (x + dx, y + dy)
        tx = self.try_get(target)

        if not tx:
            return False
        else:
            if tx == '#':
                self.dir = (self.dir + 1) % 4
            else:
                self.pos = target
        return True

    def try_get(self, grid_ref):
        x, y = grid_ref
        if x < 0 or y < 0:
            return None
        try:
            return self.grid[y][x]
        except IndexError:
            return None




def part1():
    grid = Grid()
    while grid.step():
        continue

    return len(grid.visited)

def part2():
    grid = Grid()
    while grid.step():
        continue

    count = 0
    for v in grid.visited:
        # This is really inefficient but it all runs within about 10s, so we're not optimising today
        p2 = Grid()
        x, y = v
        s = p2.grid[y]
        p2.grid[y] = s[:x] + '#' + s[x + 1:]
        while p2.step():
            if (p2.pos, p2.dir) in p2.loop_map:
                count = count + 1
                break

    return count

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')

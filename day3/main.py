#!/usr/bin/env python

import sys


def part1():
    """
    Trying very hard not to just 'import re'
    I'm sure this can be cleaned up a lot but I'm also not going to do it
    """
    score = 0
    with open('%s/input' % sys.path[0]) as f:
        for line in f:
            for i in range(len(line)):
                candidate = line[i:i + 12]
                if candidate.startswith('mul('):
                    switch_digit = False
                    a = 0
                    b = 0
                    for ch in candidate[4:]:
                        if ch == ')' and switch_digit:
                            score = score + (a * b)
                            break
                        elif ch == ',':
                            switch_digit = True
                        elif ch.isdigit():
                            if not switch_digit:
                                a = (a * 10) + int(ch)
                            else:
                                b = (b * 10) + int(ch)
                        else:
                            break
    return score

def part2():
    score = 0
    with open('%s/input' % sys.path[0]) as f:
        do = True
        for line in f:
            for i in range(len(line)):
                candidate = line[i:i + 12]
                if candidate.startswith('do()'):
                    do = True
                if candidate.startswith('don\'t()'):
                    do = False
                if do and candidate.startswith('mul('):
                    switch_digit = False
                    a = 0
                    b = 0
                    for ch in candidate[4:]:
                        if ch == ')' and switch_digit:
                            score = score + (a * b)
                            break
                        elif ch == ',':
                            switch_digit = True
                        elif ch.isdigit():
                            if not switch_digit:
                                a = (a * 10) + int(ch)
                            else:
                                b = (b * 10) + int(ch)
                        else:
                            break
    return score

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')

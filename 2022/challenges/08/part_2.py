# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the solution to the challenge #7 part 2 of the 2022 edition of Advent of Code.
"""
import sys
from time import sleep
sys.path.append('../')
from colors import bcolors

lines = []
with open("data.txt", "r") as f:
    for l in f:
        lines.append(list(l.strip()))

x_end, y_end = len(lines[0]) - 1, len(lines) - 1

def tree_scenic_score(value, x, y):
    left, right, top, bottom = 1, 1, 1, 1
    # Check left
    for i in range(x - 1, 0, -1):
        if int(lines[y][i]) >= value:
            break
        left += 1
    # Check right
    for i in range(x + 1, x_end):
        if int(lines[y][i]) >= value:
            break
        right += 1
    # Check top
    for i in range(y - 1, 0, -1):
        if int(lines[i][x]) >= value:
            break
        top += 1
    # Check bottom
    for i in range(y + 1, y_end):
        if int(lines[i][x]) >= value:
            break
        bottom += 1
    result = left * right * top * bottom
    if result > 0:
        print(f"({x}, {y}) - {value} - {left} {right} {top} {bottom} = {result}")
    return result
    

highest_score = 0
for y in range(0, y_end):
    for x in range(0, x_end):
        value = int(lines[y][x])
        if x != 0 and y != 0 and x != x_end and y != y_end:
            score = tree_scenic_score(value, x, y)
            if score > highest_score:
                highest_score = score
    print()

print(f"Highest score: {bcolors.OKGREEN}{highest_score}{bcolors.ENDC}")
        

                   





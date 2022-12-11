# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the solution to the challenge #7 part 1 of the 2022 edition of Advent of Code.
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
visible = 0

def check_visibility(value, x, y):
    left, right, top, bottom = True, True, True, True
    # Check left
    for i in range(0, x):
        if int(lines[y][i]) >= value:
            left = False
            break
    # Check right
    for i in range(x + 1, x_end + 1):
        if int(lines[y][i]) >= value:
            right = False
            break
    # Check top
    for i in range(0, y):
        if int(lines[i][x]) >= value:
            top = False
            break
    # Check bottom
    for i in range(y + 1, y_end + 1):
        if int(lines[i][x]) >= value:
            bottom = False
            break
    return left or right or top or bottom
    

for y in range(0, y_end + 1):
    curr_line_visible = 0
    for x in range(0, x_end + 1):
        value = int(lines[y][x])
        if x == 0 or y == 0 or x == x_end or y == y_end:
            print(f"{bcolors.OKGREEN}{value}{bcolors.ENDC}", end="")
            visible += 1
            curr_line_visible += 1
        elif check_visibility(value, x, y):
            print(f"{bcolors.OKGREEN}{value}{bcolors.ENDC}", end="")
            visible += 1
            curr_line_visible += 1
        else:
            print(f"{value}", end="")
    print(f"   +{bcolors.OKBLUE}{curr_line_visible}{bcolors.ENDC} = {bcolors.OKGREEN}{visible}{bcolors.ENDC}")

print("Tree count: {}".format(len(lines) * len(lines[0])))
print("Visible: {}".format(visible))
        

                   





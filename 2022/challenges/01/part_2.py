# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a script to solve the first challenge 
of the 2022 edition of the Advent of Code."""

cals = []
cur = 0
with open("data.txt", "r") as f:
    for line in f:
        if line == "\n":
            cals.append(cur)
            cur = 0
        else:
            cur += int(line)

total_max = 0
for i in range(3):
    cur_max = max(cals)
    total_max += cur_max
    cals.remove(cur_max)

print(total_max)

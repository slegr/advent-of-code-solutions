# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a script to solve the first challenge 
of the 2022 edition of the Advent of Code."""

max = cur = 0
with open("data.txt", "r") as f:
    for line in f:
        if line == "\n":
            if cur > max:
                max = cur
            cur = 0
        else:
            cur += int(line)
print(max)

# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the solution to the challenge #4 part 1 of the 2022 edition of Advent of Code.
"""


overlap_count = 0
line_number = 0
with open("data.txt", "r") as f:
    for line in f:
        line_striped = line.strip()
        pair_ranges = line_striped.split(",")
        range_elf1 = pair_ranges[0].split("-")
        range_elf2 = pair_ranges[1].split("-")
        range_elf1 = [int(range_elf1[0]), int(range_elf1[1])]
        range_elf2 = [int(range_elf2[0]), int(range_elf2[1])]
        # check if one list fully contains the other
        if range_elf1[0] <= range_elf2[0] <= range_elf2[1] <= range_elf1[1]:
            print(f"{line_number}: Elf1 {str(range_elf1):12} contains {range_elf2}")
            overlap_count += 1
        elif range_elf2[0] <= range_elf1[0] <= range_elf1[1] <= range_elf2[1]:
            print(f"{line_number}: Elf2 {str(range_elf2):12} contains {range_elf1}")
            overlap_count += 1
        line_number += 1

print(overlap_count)




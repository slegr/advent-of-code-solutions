# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a script to solve the third challenge, part 2,
    of the 2022 edition of the Advent of Code."""

import string

# Letters
letters = list(string.ascii_letters)

# Dictoinary of association between each letter and its corresponding priority, from 1 to 52
prio_dict = {letter: i for i, letter in enumerate(letters, 1)}

total_priorities = 0
with open("data.txt", "r") as f:
    for line1 in f:
        line1 = line1.strip()
        line2 = next(f).strip()
        line3 = next(f).strip()
        common_elements = list(
            set(line1).intersection(line2, line3)
        )
        print(line1)
        print(line2)
        print(line3)
        print(common_elements)
        print("\n")

        # Find the priority of the most common letter
        most_comm_letter_prio = prio_dict[common_elements[0]]
        total_priorities += most_comm_letter_prio

print(total_priorities)


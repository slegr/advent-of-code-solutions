# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a script to solve the third challenge, part 1,
    of the 2022 edition of the Advent of Code."""

import string

# Letters
letters = list(string.ascii_letters)

# Dictoinary of association between each letter and its corresponding priority, from 1 to 52
prio_dict = {letter: i for i, letter in enumerate(letters, 1)}

total_priorities = 0
with open("data.txt", "r") as f:
    for line in f:
        line_striped = line.strip()
        line_splitted = list(line_striped)
        # dictionary of each letter in splitted line and its number of occurences
        letter_dict = {letter: line_splitted.count(letter) for letter in line_splitted}

        # Split the line in two parts
        first_half = line_splitted[:len(line) // 2]
        second_half = line_splitted[len(line) // 2:]
        
        # Compare both parts and find letters appearing in both parts
        common_letters = [letter for letter in first_half if letter in second_half]
        most_comm_letter = common_letters[0]

        # Find the priority of the most common letter
        most_comm_letter_prio = prio_dict[most_comm_letter]
        total_priorities += most_comm_letter_prio

print(total_priorities)


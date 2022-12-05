# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the solution to the challenge #5 part 1 of the 2022 edition of Advent of Code.
"""

# data header
header_line_count = 8
header_column_count = 36
header_cols_with_data = [1, 5, 9, 13, 17, 21, 25, 29, 33]

# stacks
stack_count = 9
stack_height = 8
stacks = [[] for i in range(stack_count)]

# moves
moves_start_line = 10
moves = [] # (quantity, sfrom, sto)

# result
str_result = ""

def read_header(line):
    for i, value in enumerate(header_cols_with_data):
        if value > len(line):
            break
        if line[value] != " ":
            stacks[i].append(line[value])

current_line = 0
with open("data.txt", "r") as f:
    for line in f:
        if current_line < header_line_count:
            read_header(line)
        elif current_line >= moves_start_line:
            line = line.strip().split(" ")
            quantity = int(line[1])
            sfrom = int(line[3])
            sto = int(line[5])
            moves.append((quantity, sfrom, sto))   
        current_line += 1

print("\nInitial stacks:")
for s in stacks:
    s.reverse()
    print(s)

for m in moves:
    quantity = m[0]
    sfrom = m[1] - 1
    sto = m[2] - 1
    for i in range(quantity):
        crate = stacks[sfrom].pop()
        stacks[sto].append(crate)

print("\nFinal stacks:")
for s in stacks:
    print(s)

for s in stacks:
    str_result += str(s.pop())

print(str_result)




# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the solution to the challenge #12 part 1 of the 2022 edition of Advent of Code.
"""
import sys
from time import sleep
sys.path.append('../')
from colors import bcolors

def read_input():
    with open("data_small.txt", "r") as f:
        for l in f:
            lines.append(list(l.strip()))

class Tryout():
    def __init__(self):
        self.positions = []
        self.last_position = None

    def add_position(self, x, y):
        self.positions.append((x, y))
        self.last_position = (x, y)

lines = []
start = None
end = None
read_input()

# Find S (start) and E (end)
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "S":
            start = (x, y)
        if char == "E":
            end = (x, y)

all_tryout = []
current_tryout = Tryout()
current_tryout.add_position(start[0], start[1])   # Add start position
searched_pos = [current_tryout.last_position]

def get_letters_in_priority(letter, letter_list):
    letters_plus1 = []
    letters_same = []
    for l in letter_list:
        if letter == "z" and l == "E":
            return ["E"]
        elif ord(letter) - ord(l) == -1:
            letters_plus1.append(l)
        elif ord(letter) - ord(l) == 0:
            letters_same.append(l)
    return letters_plus1 + letters_same

def search_path(x, y):
    cur_val = lines[y][x]
    cur_val = "a" if cur_val == "S" else cur_val
    left_pos, right_pos, up_pos, down_pos = (x-1, y), (x+1, y), (x, y-1), (x, y+1)
    left_val = lines[y][x-1] if x-1 >= 0 else "-"
    right_val = lines[y][x+1] if x+1 < len(lines[0]) else "-"
    up_val = lines[y-1][x] if y-1 >= 0 else "-"
    down_val = lines[y+1][x] if y+1 < len(lines) else "-"

    values = [left_val, right_val, up_val, down_val]
    positions = [left_pos, right_pos, up_pos, down_pos]

    letters_prio = get_letters_in_priority(cur_val, values)
    print(f"cur_val={cur_val}, cur_pos={(x,y)}, letters_prio={letters_prio}, positions={positions}")


    for val in letters_prio:
        if val == "E":
            print(f"Found END! after {len(current_tryout.positions)} steps")
            return
        i = values.index(val)
        if positions[i] not in searched_pos:
            searched_pos.append(positions[i])
            current_tryout.add_position(positions[i][0], positions[i][1])
            search_path(positions[i][0], positions[i][1])
    

search_path(current_tryout.last_position[0], current_tryout.last_position[1])


# found = False
# while not found:
#     x, y = current_tryout.last_position
#     print(x, y, lines[y][x], current_tryout.positions)

#     cur_val = lines[y][x]
#     cur_val = "a" if cur_val == "S" else cur_val

#     left_pos, left_val = (x-1, y), lines[y][x-1]
#     right_pos, right_val = (x+1, y), lines[y][x+1]
#     up_pos, up_val = (x, y-1), lines[y-1][x]
#     down_pos, down_val = (x, y+1), lines[y+1][x]

#     print(left_pos, right_pos, up_pos, down_pos)

#     if left_pos[0] >= 0 and ((x,y) not in current_tryout.positions) and (ord(left_val) - ord(cur_val) == 1 or left_val == "E"):
#         print("Left")
#         current_tryout.add_position(left_pos[0], left_pos[1])
#     elif right_pos[0] < len(lines[0]) and ((x,y) not in current_tryout.positions)  and (ord(right_val) - ord(cur_val) == 1 or right_val == "E"):
#         print("Right")
#         current_tryout.add_position(right_pos[0], right_pos[1])
#     elif up_pos[1] >= 0 and ((x,y) not in current_tryout.positions)  and (ord(up_val) - ord(cur_val) == 1 or up_val == "E"):
#         print("Up")
#         current_tryout.add_position(up_pos[0], up_pos[1])
#     elif down_pos[1] < len(lines) and ((x,y) not in current_tryout.positions)  and (ord(down_val) - ord(cur_val) == 1 or down_val == "E"):
#         print("Down")
#         current_tryout.add_position(down_pos[0], down_pos[1])

# print(current_tryout.positions)
# print(len(current_tryout.positions))
        
    

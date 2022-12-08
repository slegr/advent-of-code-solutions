# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the solution to the challenge #6 part 2 of the 2022 edition of Advent of Code.
"""

from time import sleep
# import bcolors from colors.py in challenges folder
import sys
sys.path.append('../')
from colors import bcolors


start_of_packet = 0
with open("data.txt", "r") as f:
    line = f.readline().strip()
    car_list = list(line)

    for i in range(13, len(car_list)):
        letters_14 = [car_list[x] for x in range(i-14, i)]
        letters_set = set(letters_14)
        if len(letters_set) == 14:
            print(f"{bcolors.OKBLUE}{letters_set}{bcolors.ENDC}")
            print(f"{bcolors.OKBLUE}{i+1} letters processed{bcolors.ENDC}")
            break







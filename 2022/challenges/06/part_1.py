# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the solution to the challenge #6 part 1 of the 2022 edition of Advent of Code.
"""

start_of_packet = 0
with open("data.txt", "r") as f:
    line = f.readline().strip()
    car_list = list(line)

    for i in range(3, len(car_list)):
        four_letter = set((car_list[i-3], car_list[i-2], car_list[i-1], car_list[i]))
        if len(four_letter) == 4:
            print(four_letter)
            print(f"{i+1} letters processed")
            break







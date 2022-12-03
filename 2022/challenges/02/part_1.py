# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a script to solve the second challenge 
of the 2022 edition of the Advent of Code.
Rules: X = 1, Y = 2, Z = 3, Lose = 0, Draw = 3, Win = 6"""

hands = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

rules = {
    (1, 1): False,
    (1, 2): True,
    (1, 3): False,
    (2, 1): False,
    (2, 2): False,
    (2, 3): True,
    (3, 1): True,
    (3, 2): False,
    (3, 3): False
}
total_points = 0
with open("data.txt", "r") as f:
    for line in f:
        opp_letter, me_letter = line.split()
        opp = ord(opp_letter) - 64
        me = ord(me_letter) - 64 - 23
        diff = opp - me
        is_win = rules[(opp, me)]
        win_point = 6 if is_win else 3 if diff == 0 else 0
        round_points = win_point + me
        total_points += round_points
        print(f"\n{hands[opp]} {opp_letter} vs {hands[me]} {me_letter} == {is_win}")
        print(f"{opp} - {me} = {diff}")
        print(f"Win points: {win_point}")
        print(f"Hand Points: {me}")
        print(f"Round points: {round_points}")

print(total_points)


# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a script to solve the second challenge, part 2,
    of the 2022 edition of the Advent of Code.
Points: A = 1, B = 2, C = 3, Lose = 0, Draw = 3, Win = 6"""

def win(hand):
    if hand == 'A':
        return ('B', 2, 6)
    elif hand == 'B':
        return ('C', 3, 6)
    elif hand == 'C':
        return ('A', 1, 6)

def lose(hand):
    if hand == 'A':
        return ('C', 3, 0)
    elif hand == 'B':
        return ('A', 1, 0)
    elif hand == 'C':
        return ('B', 2, 0)

def draw(hand):
    if hand == 'A':
        return ('A', 1, 3)
    elif hand == 'B':
        return ('B', 2, 3)
    elif hand == 'C':
        return ('C', 3, 3)


results_dict = {
    'X': lose,
    'Y': draw,
    'Z': win
}

total_points = 0
with open("data.txt", "r") as f:
    for line in f:
        opponent_hand, result = line.split()
        # find the hand to get result
        func = results_dict[result]
        my_hand, hand_points, win_points = func(opponent_hand)
        round_points = hand_points + win_points
        print(f"\n{opponent_hand} vs ? = {func.__name__} -> {my_hand}")
        print(f"Round points: {round_points}")
        total_points += round_points
        

print(total_points)


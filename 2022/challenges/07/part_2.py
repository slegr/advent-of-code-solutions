# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the solution to the challenge #7 part 1 of the 2022 edition of Advent of Code.
"""
import sys
sys.path.append('../')
from colors import bcolors

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size

    def __str__(self):
        return "File: " + self.name + " Size: " + str(self.size)

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

    def add_child(self, child):
        self.children.append(child)

    def add_file(self, file):
        self.files.append(file)

    def set_size(self, size):
        self.size = size

    def get_size(self):
        size = 0
        for child in self.children:
            size += child.get_size()
        for file in self.files:
            size += file.get_size()
        return size

    def get_full_path(self):
        return self.parent.get_full_path() + self.name + "/"

    def __str__(self):
        ch = [c.name for c in self.children]
        return "Directory: " + self.name \
            + " Size: " + str(self.get_size()) \
            + " Parent: " + (self.parent.name if self.parent else "None") \
            + " Children: " + str(ch) \

    def get_valid_children_sizes(self, level):
        total = 0
        for c in self.children:
            s = c.get_size()
            if s <= 100000:
                print(bcolors.OKGREEN + " - " * level + c.name + " size: " + str(s) + bcolors.ENDC)
                total += s
            else:
                print(bcolors.FAIL + " - " * level + c.name + " size: " + str(s) + bcolors.ENDC)
            total += c.get_valid_children_sizes(level + 1)  
        return total

    def get_child_closest_to_size(self, size):
        closest_size = 30000000
        for c in self.children:
            children_best_value = c.get_child_closest_to_size(size)
            if children_best_value  >= size and children_best_value < closest_size:
                closest_size = children_best_value
            c_size = c.get_size()
            if c_size >= size and c_size < closest_size:
                closest_size = c_size
            
        return closest_size


base_directory = Directory("/", None)
current_dir = base_directory

with open("data.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith("$ cd"):
            # Change directory
            dir_name = line.split(" ")[2]
            if dir_name == "..":
                current_dir = current_dir.parent if current_dir.parent else current_dir
                continue
            elif dir_name == current_dir.name:
                continue
            # Check if directory exists
            child = current_dir.get_child(dir_name)
            if child is None:
                # Create new directory
                child = Directory(dir_name, current_dir)
                current_dir.add_child(child)
            current_dir = child

        elif line.startswith("$ ls"):
            continue

        elif line.startswith("dir"):
            # Create new directory
            dir_name = line.split(" ")[1]
            child = Directory(dir_name, current_dir)
            current_dir.add_child(child)
            
        else:
            # Create new file
            file_size = int(line.split(" ")[0])
            file_name = line.split(" ")[1]
            file = File(file_name, file_size)
            current_dir.add_file(file)
            

print(base_directory)
print(base_directory.get_valid_children_sizes(0))

current_storage_use = base_directory.get_size()
unused_space = 70000000 - current_storage_use
space_to_delete = 30000000 - unused_space
print("Current storage use: " + str(current_storage_use))
print("Unused space: " + str(unused_space))
print("Space to delete: " + str(space_to_delete))

best_size = base_directory.get_child_closest_to_size(space_to_delete)
print("Best size: " + str(best_size))








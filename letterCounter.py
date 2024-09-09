# silly little program to count instances of a letter in a text file

import re

file_name = input("enter file name: ")

file_handle = open(file_name)

letter = input("enter a letter to count: ")

count = 0
for line in file_handle:
    line = line.rstrip()
    letter_instances = re.findall(letter, line)
    count = count + len(letter_instances)

if count == 1: print("the letter", letter, "appears 1 time")
else: print("the letter", letter, "appears", count, "times")
# -*- coding: utf-8 -*-

# Beginning Frequency
frequency = 0

# Open the file
with open("input.txt") as file:
    # Read all lines from file
    data = file.readlines()

    # For each line add/subract for freq
    for line in data:
        words = line.split()
        frequency += int(words[0])

print("FINAL FREQUENCY: {}".format(frequency))


import itertools
frequencies = [int(num) for num in open("input.txt").readlines()]
print("Sum: " + sum(frequencies))

frequnecies = 0
frequencies_seen = set([0])
for num in itertools.cycle(data):
    frequnecies += num
    if frequnecies in frequencies_seen:
        print("First Duplicate: " + frequnecies)
        break
    frequencies_seen.add(freq)
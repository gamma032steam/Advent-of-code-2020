import math 
import functools
import re
import random
import collections

def solve1(adapters):
    adapters.sort()
    differences = [0, 0, 1]
    last = 0
    for jolts in adapters:
        diff = jolts - last
        if diff == 1:
            differences[0] += 1
        elif diff == 2:
            differences[1] += 1
        else:
            differences[2] += 1
        last = jolts
    print(differences[0]*differences[2])

def solve2(adapters):
    adapters.sort()
    num_ways = [0] * len(adapters)
    # 1 way to get to voltages 1-3
    for i in range(len(adapters)):
        if adapters[i] <= 3:
            num_ways[i] += 1
        else:
            break
    # add up
    for i in range(len(adapters)):
        j = i+1
        while j < len(adapters) and adapters[j] - adapters[i] <= 3:
            num_ways[j] += num_ways[i]
            j += 1

    print(num_ways[-1])


if __name__ == "__main__":
    with open('./input/10-input.txt') as f:
        data = f.read().splitlines()
        data = list(map(int, data))
        solve1(data)
        solve2(data)
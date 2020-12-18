import math 
import functools
import re
import random
import collections

INVALID_NUM = 552655238

def solve1(data):
    data = list(map(int, data))
    seen = dict()
    for i in range(len(data)):
        target = data[i]
        if i >= 25:
            # two sum
            possible = False
            for j in range(i-25, i):
                rem = target-data[j]
                if rem in seen and seen[rem] >= i-25 and seen[rem] < i:
                    possible = True
            if not possible:
                print(data[i])
                return
        seen[target] = i

def solve2(data):
    data = list(map(int, data))
    total = 0
    f = 0
    for i in range(len(data)):
        total += data[i]   
        while total > INVALID_NUM:
            total -= data[f]
            f += 1
        if total == INVALID_NUM and i - f >= 2:
            sequence = data[f:i+1]
            print(min(sequence) + max(sequence)) 
            return

if __name__ == "__main__":
    with open('./input/9-input.txt') as f:
        data = f.read().splitlines()
        solve1(data)
        solve2(data)
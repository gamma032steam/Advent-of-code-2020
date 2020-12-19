import math 
import functools
import re
import random
import collections

def solve1(instructions):
    x = y = orientation = 0
    for line in instructions:
        match = re.match('^(\w)(\d+)$', line)
        direction = match.group(1)
        mag = int(match.group(2))
        if direction == 'N' or (direction == 'F' and orientation == 90):
            y += mag
        elif direction == 'S' or (direction == 'F' and orientation == 270):
            y -= mag
        elif direction == 'E' or (direction == 'F' and orientation == 0):
            x += mag
        elif direction == 'W' or (direction == 'F' and orientation == 180):
            x -= mag
        elif direction == 'L':
            orientation = (orientation + mag) % 360
        elif direction == 'R':
            orientation = (orientation - mag + 360) % 360
    print(abs(x) + abs(y))

def solve2(instructions):
    x = y = 0
    wp_x, wp_y = 10, 1
    for line in instructions:
        match = re.match('^(\w)(\d+)$', line)
        direction = match.group(1)
        mag = int(match.group(2))
        if direction == 'N':
            wp_y += mag
        elif direction == 'S':
            wp_y -= mag
        elif direction == 'E':
            wp_x += mag
        elif direction == 'W':
            wp_x -= mag
        elif direction == 'L' or direction == 'R':
            orientation = mag if direction == 'L' else 360-mag
            wp_x, wp_y = rotate(wp_x, wp_y, orientation)
        elif direction == 'F':
            x += wp_x * mag
            y += wp_y * mag
    print(abs(x) + abs(y))

def rotate(x, y, degs):
    # rotate clockwise
    c = round(math.cos(math.radians(degs)))
    s = round(math.sin(math.radians(degs)))
    return (x*c - y*s, x*s + y*c)

if __name__ == "__main__":
    with open('./input/12-input.txt') as f:
        data = f.read().splitlines()
        solve1(data)
        solve2(data)
import math 
import functools
import re
import random
from copy import deepcopy
import collections

def solve1(seats):
    changes = 1
    taken_seats = 0
    while changes != 0:
        changes = 0
        taken_seats = 0
        # init a new grid
        new_seats = []
        for i in range(len(seats)):
            new_seats.append([])
            for j in range(len(seats[0])):
                new_seats[i].append(' ')
        for row in range(len(seats)):
            for col in range(len(seats[0])):
                # rule 1: become occupied if no adjacent seats are occupied
                # rule 2: leave if 4 or more adjacent seats are occupied
                # rule 3: if none of the above, keep the same!
                adj = count_adjacent(seats, row, col) 
                if seats[row][col] == 'L' and adj == 0:
                    new_seats[row][col] = '#'
                    taken_seats += 1
                    changes += 1
                elif seats[row][col] == '#' and adj >= 4:
                    new_seats[row][col] = 'L'
                    changes += 1
                else:
                    new_seats[row][col] = seats[row][col]   
                    if new_seats[row][col] == '#': taken_seats += 1
        seats = deepcopy(new_seats)
    print(taken_seats)

def count_adjacent(seats, row, col):
    dirs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    cnt = 0
    for direction in dirs:
        new_pos = (row + direction[0], col + direction[1])
        if new_pos[0] >= 0 and new_pos[0] < len(seats) and new_pos[1] >= 0 and new_pos[1] < len(seats[0]):
            if seats[new_pos[0]][new_pos[1]] == '#':
                cnt += 1
    return cnt

def solve2(seats):
    changes, taken_seats = 1, 0
    while changes != 0:
        changes = taken_seats = 0
        # init a new grid
        new_seats = []
        for i in range(len(seats)):
            new_seats.append([])
            for j in range(len(seats[0])):
                new_seats[i].append(' ')

        for row in range(len(seats)):
            for col in range(len(seats[0])):
                # rule 1: become occupied if no adjacent seats are occupied
                # rule 2: leave if 5 or more adjacent seats are occupied
                # rule 3: if none of the above, keep the same!
                adj = count_visible(seats, row, col) 
                if seats[row][col] == 'L' and adj == 0:
                    new_seats[row][col] = '#'
                    taken_seats += 1
                    changes += 1
                elif seats[row][col] == '#' and adj >= 5:
                    new_seats[row][col] = 'L'
                    changes += 1
                else:
                    new_seats[row][col] = seats[row][col]   
                    if new_seats[row][col] == '#': taken_seats += 1
        seats = deepcopy(new_seats)
    print(taken_seats)

def count_visible(seats, row, col):
    dirs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    cnt = 0
    for direction in dirs:
        new_pos = (row, col)
        while True:
            new_pos = (new_pos[0] + direction[0], new_pos[1] + direction[1])
            if new_pos[0] >= 0 and new_pos[0] < len(seats) and new_pos[1] >= 0 and new_pos[1] < len(seats[0]):
                if seats[new_pos[0]][new_pos[1]] == '#':
                    cnt += 1
                    break
                elif seats[new_pos[0]][new_pos[1]] == 'L':
                    break
            else:
                break
    return cnt

def print_grid(seats):
    print("GRID:")
    for line in seats:
        print(str(line))                    

if __name__ == "__main__":
    with open('./input/11-input.txt') as f:
        data = f.read().splitlines()
        data = map(list, data)
        solve1(data)
        solve2(data)
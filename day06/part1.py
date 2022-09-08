import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    points = [tuple(map(int, i.strip().split(","))) for i in inf]
    areas = [0 for _ in points]
    infinite = [False for _ in points]

    min_x = min(points)[0]
    max_x = max(points)[0]
    min_y = min(points, key=lambda x: x[1])[1]
    max_y = max(points, key=lambda x: x[1])[1]

    for x, y in it.product(range(min_x, max_x + 1), range(min_y, max_y + 1)):
        min_dist = 10000000000000
        valid = True
        index = -1

        for i, (px, py) in enumerate(points):
            dist = abs(x - px) + abs(y - py)
            if dist == min_dist:
                valid = False
            elif dist < min_dist:
                valid = True
                min_dist = dist
                index = i

        if not valid:
            continue

        areas[index] += 1

        if x == min_x or x == max_x or y == min_y or y == max_y:
            infinite[index] = True

    outf.write(str(max(a for i, a in enumerate(areas) if not infinite[i])))

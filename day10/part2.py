import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    pattern = re.compile(
        r"position=<\s?(-?\d+),\s*(-?\d+)> velocity=<\s?(-?\d+),\s*(-?\d+)>")
    points = [(int(n) for n in pattern.match(i).groups()) for i in inf]

    for s in it.count():
        min_x = 1000000
        min_y = 1000000
        max_x = -1000000
        max_y = -1000000

        for i, (x, y, vx, vy) in enumerate(points):
            points[i] = x + vx, y + vy, vx, vy

            min_y = min(min_y, y + vy)
            min_x = min(min_x, x + vx)
            max_y = max(max_y, y + vy)
            max_x = max(max_x, x + vx)

        if max_y - min_y <= 10:
            outf.write(str(s + 1))
            break

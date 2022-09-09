import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    pattern = re.compile(
        r"position=<\s?(-?\d+),\s*(-?\d+)> velocity=<\s?(-?\d+),\s*(-?\d+)>")
    points = [(int(n) for n in pattern.match(i).groups()) for i in inf]

    while True:
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

        w = max_x - min_x + 1
        h = max_y - min_y + 1
        if max_y - min_y <= 10:
            message = [' ' for _ in range(w * h)]

            for x, y, _, _ in points:
                x -= min_x
                y -= min_y
                message[x + y * w] = '#'

            print('\n'.join(''.join(l) for l in mit.chunked(message, w)))
            message = input()

            if message:
                outf.write(message)
                break

import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    points = [tuple(map(int, i.strip().split(","))) for i in inf]

    outf.write(
        str(
            len([(x, y)
                 for x, y in it.product(
                     range(min(points)[0],
                           max(points)[0] + 1),
                     range(
                         min(points, key=lambda x: x[1])[1],
                         max(points, key=lambda x: x[1])[1] + 1))
                 if sum(abs(x - px) + abs(y - py) for px, py in points) < 10000
                ])))

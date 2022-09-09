import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    serial_number = int(inf.readline().strip())
    d = {}
    max_power = 0
    coords = 0, 0, 0

    for size in range(1, 31):
        print(size, end='\r')
        for x, y in it.product(range(1, 302 - size), range(1, 302 - size)):
            if size == 1:
                d[x, y, size] = (((x + 10) * y + serial_number) *
                                 (x + 10) // 100 % 10) - 5
            else:
                d[x, y, size] = d[x, y, size - 1] + sum(
                    d[x + dx, y + size - 1, 1] for dx in range(size)) + sum(
                        d[x + size - 1, y + dy, 1]
                        for dy in range(size)) - d[x + size - 1, y + size - 1,
                                                   1]

            if d[x, y, size] > max_power:
                max_power = d[x, y, size]
                coords = x, y, size

    outf.write(f"{coords[0]},{coords[1]},{coords[2]}")

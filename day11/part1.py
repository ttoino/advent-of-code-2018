import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    serial_number = int(inf.readline().strip())
    d = {}
    max_power = 0
    coords = 0, 0

    for x, y in list(it.product(range(1, 301), range(1, 301)))[::-1]:
        d[x, y] = (((x + 10) * y + serial_number) * (x + 10) // 100 % 10) - 5

        if x <= 298 and y <= 298:
            power = sum(d[x + px, y + py] for px in range(3) for py in range(3))
            if power > max_power:
                max_power = power
                coords = x, y

    outf.write(f"{coords[0]},{coords[1]}")

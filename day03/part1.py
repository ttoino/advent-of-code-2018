import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    c = Counter()
    pattern = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")

    for i in inf:
        m = pattern.match(i)

        for p in it.product(range(int(m[2]),
                                  int(m[2]) + int(m[4])),
                            range(int(m[3]),
                                  int(m[3]) + int(m[5]))):
            c[p] += 1

    outf.write(str(len([c for p, c in c.items() if c >= 2])))

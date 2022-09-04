import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    for a, b in it.combinations(inf, 2):
        s = "".join(a for a, b in zip(a.strip(), b.strip()) if a == b)
        if len(s) == 25:
            outf.write(s)
            break

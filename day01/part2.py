import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    f = 0
    s = {0}

    for i in it.cycle(inf):
        f += int(i.strip())
        if f in s:
            outf.write(str(f))
            break
        s.add(f)

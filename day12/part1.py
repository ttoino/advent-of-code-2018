import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, defaultdict

with open("input") as inf, open("part1.out", "w+") as outf:
    offset = 0
    pots = tuple(c == "#" for c in inf.readline().strip().split()[-1])
    patterns = {tuple(c == "#" for c in line.strip().split(" => ")[0]): line.strip().split(" => ")[1] == "#" for line in inf.readlines()[1:]}

    for _ in range(20):
        pots = (False, False, False, False, *pots, False, False, False, False)
        offset -= 2
        pots = tuple(patterns[window] for window in mit.windowed(pots, 5, fillvalue=False))
        
        while not pots[0]:
            pots = pots[1:]
            offset += 1

        while not pots[-1]:
            pots = pots[:-1]

    outf.write(str(sum(i + offset for i, pot in enumerate(pots) if pot)))

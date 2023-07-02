import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

ITERS = 50_000_000_000

with open("input") as inf, open("part2.out", "w+") as outf:
    offset = 0
    pots = tuple(c == "#" for c in inf.readline().strip().split()[-1])
    patterns = {tuple(c == "#" for c in line.strip().split(" => ")[0]): line.strip().split(" => ")[1] == "#" for line in inf.readlines()[1:]}

    for i in range(ITERS):
        print(i, end="\r")

        oldpots = pots
        oldoffset = offset

        pots = tuple(patterns[window] for window in mit.windowed((False, False, False, False, *pots, False, False, False, False), 5, fillvalue=False))
        offset -= 2
        
        while not pots[0]:
            pots = pots[1:]
            offset += 1

        while not pots[-1]:
            pots = pots[:-1]
        
        if oldpots == pots:
            offset += (offset - oldoffset) * (ITERS - i - 1)
            break

    outf.write(str(sum(i + offset for i, pot in enumerate(pots) if pot)))



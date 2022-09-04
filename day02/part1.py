import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    twos, threes = 0, 0

    for i in inf:
        c = Counter(i.strip()).values()

        twos += 2 in c
        threes += 3 in c

    outf.write(str(twos * threes))

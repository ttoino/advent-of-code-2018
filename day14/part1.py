import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    n = int(inf.readline())
    scores = [3, 7]
    pos1 = 0
    pos2 = 1

    while len(scores) < n + 10:
        new_score = scores[pos1] + scores[pos2]
        scores.extend(map(int, str(new_score)))
        pos1 += 1 + scores[pos1]
        pos1 %= len(scores)
        pos2 += 1 + scores[pos2]
        pos2 %= len(scores)

    outf.write("".join(map(str, scores[n:])))

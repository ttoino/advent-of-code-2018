import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    n = list(map(int, inf.readline().strip()))
    scores = [3, 7]
    pos1 = 0
    pos2 = 1

    while True:
        new_score = map(int, str(scores[pos1] + scores[pos2]))
        scores.append(next(new_score))
        if scores[-len(n):] == n:
            break
        if (x := next(new_score, None)) is not None:
            scores.append(x)
            if scores[-len(n):] == n:
                break
        pos1 += 1 + scores[pos1]
        pos1 %= len(scores)
        pos2 += 1 + scores[pos2]
        pos2 %= len(scores)

    outf.write(str(len(scores) - len(n)))

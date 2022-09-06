import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


def react(s: str):
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1].swapcase():
            s = s[:i] + s[i + 2:]
            i -= 1
            continue
        i += 1

    return len(s)


with open("input") as inf, open("part1.out", "w+") as outf:
    s = inf.readline().strip()
    outf.write(str(react(s)))

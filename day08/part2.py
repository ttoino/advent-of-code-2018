import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, defaultdict


def parse(l: list[int]) -> tuple[list[int], int]:
    children_count, entries, *l = l

    children = defaultdict(lambda: 0)
    for i in range(children_count):
        l, s = parse(l)
        children[i + 1] = s

    return l[entries:], sum(l[:entries]) if children_count == 0 else sum(
        children[i] for i in l[:entries])


with open("input") as inf, open("part2.out", "w+") as outf:
    outf.write(str(parse([int(n) for n in inf.readline().strip().split()])[1]))
